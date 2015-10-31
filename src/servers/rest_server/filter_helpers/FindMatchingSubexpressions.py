"""
The function find_matches takes as input two parsed and evaluated trees, one for the correct answer and one for the attempt.
It finds the subexpressions that match between the correct and the attempt and returns it as a list of 
tuples of the form (node,value,answer_part,attempt_part)

The other functions are helpers that are called from find_matches.
"""
import sys
from collections import deque
from string import strip, replace
import json

#from webwork_parser import parse_webwork

# Set up a logging object
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
#logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def flatten(tree,tag):
    logger.debug('flattening: '+str(tree))
    List=[]
    Queue=deque([tree])
    try:
        while Queue:
            current=Queue.popleft()
            logger.debug('current='+str(current)+' Queue='+str(Queue))
            if type(current)==list: 
                if isinstance(current[0],basestring):
                    List.append([current[1],tag,current])
                elif isinstance(current[0][0],basestring) and isinstance(current[0][1],(int, long, float, complex)) and type(current[0][2])==list:
                    List.append([current[0][1],tag,current])
                    Queue.extend(current[1:])
                else:
                    logger.error('parse error (is list): \ncurrent=%s, \ntree=%s'%(str(current),str(tree)))
                    return []
            else:
                logger.error('parse error (not list): \ncurrent=%s, \ntree=%s'%(str(current),str(tree)))
                return []
    except Exception as error:
        logger.exception(error)
        logger.error('current='+str(current))
        return []
    List=sorted(List,key=lambda x: x[0])
    return List

def find_Hits(List,tol = 1+1e-6):
    """ Given a combined list of subtrees from both attempt and answer,
    sorted by value, find the matching pairs of trees
    tol is the tolerance used to define which pairs of values match. 
    Needed because different expressions get different roundoff error
    """
    Hits=[]
    item1=List[0]
    for item2 in List[1:]:
        logger.debug(str(item1[:2])+str(item2[:2]))
        ratio=item1[0]/item2[0]
        if item1[1]!=item2[1] and ratio <tol and ratio>(1/tol):
            if item1[1]=='c':
                Hits.append((item1,item2))
            elif item2[1]=='c':
                Hits.append((item2,item1))
            else:
                logger.error("Error in find_Hits. Neither item labeled c")
        item1=item2
    return Hits

def get_span(tree):
    if tree[2][0]=='X':
        return tree[2][2]
    elif type(tree[2][0])==list:
        return tree[2][0][2]
    else:
        logger.error('Error in get_span')
        return None
    
def find_dominating_hits(Hits,answer,attempt):
    for i in range(len(Hits)):
        for j in range(len(Hits)):
            if i==j:
                continue
            span1=get_span(Hits[i][0])
            span2=get_span(Hits[j][0])
            if span1[0]<=span2[0] and span1[1]>=span2[1]:
                logger.debug(str(span1)+' dominates '+str(span2))
                Hits[j][0][1]='dc'
    
    final_matches=[]
    for hit in Hits:
        if hit[0][1]=='c':
            value=hit[0][0]
            span_c=get_span(hit[0])
            span_a=get_span(hit[1])
            logger.debug('answer:'+str(answer)+str(span_c))
            logger.debug('attempt:'+str(attempt)+str(span_a))
            answer_part=answer[span_c[0]:span_c[1]+1]
            attempt_part = attempt[span_a[0]:span_a[1]+1]
            logger.debug('answer part'+str(answer_part))
            logger.debug('attempt part'+str(attempt_part))
            logger.debug('hit part='+str(hit[0][2][0]))
            if hit[0][2][0]=='X':
                node=hit[0][2][3]
            else:
                node=hit[0][2][0][3]
            final_matches.append((node,value,answer_part,attempt_part))
    return final_matches

def find_matches(params):

    attempt=params['attempt']
    logger.debug( 'attempt: '+str(attempt))
    attempt_tree=params['att_tree']
    logger.debug('calling flatten on '+str(attempt_tree))
    attempt_list=flatten(attempt_tree,'t')
    logger.debug( 'attempt list:\n'+str(attempt_list))
    
    answer=params['answer']
    logger.debug( 'answer: '+str(answer))
    answer_tree=params['ans_tree']
    logger.debug('calling flatten on '+str(answer_tree))
    answer_list=flatten(answer_tree,'c')
    logger.debug('answer list\n'+str(answer_list))

    combined_list=sorted(answer_list+attempt_list,key=lambda x: x[0])
    logger.debug('combined list\n'+str(combined_list))

    Hits=find_Hits(combined_list)
    logger.debug('Hits:\n'+str(Hits))

    final_matches=find_dominating_hits(Hits,answer,attempt)
    
    return final_matches

if __name__=="__main__":
    sys.path.append('../src')
    from parsetrees.expr_parser.Eval_parsed import parse_and_eval
    from collections import Counter

    if len(sys.argv)==3:   #parameters are two expressions
        params={}
        params['answer']=sys.argv[1]
        params['attempt']=sys.argv[2]
        params['ans_tree']=parse_and_eval(params['answer'])
        params['att_tree']=parse_and_eval(params['attempt'])
        print 'params=',params
        final_pairs=find_matches(params)
        for item in final_pairs:
            print "node=%s, value=%s, The piece %s in your answer is correct, it can also be expressed as %s"%(item[0],item[1],item[3],item[2])

    elif len(sys.argv)==2: # param is the name of a file containing a dump of attempts with their parse trees and variables
        file=open(sys.argv[1],'r')
        print file.readline()
        print file.readline()

        Clusters=Counter()
        Reps={}
        i=1
        for line in file.readlines():
            i+=1
            if len(line)>1000:
                print 'long line error in line',i
                continue
            print line,
            params=json.loads(line)
            print 'params=',params
            params['attempt'] = ''.join(params['attempt'].split()) # remove whitespaces
            if params['ans_tree']==None:
                print '-'*50,'error parsing answer'
                params['ans_tree']=parse_and_eval(params['answer'])
            final_pairs=find_matches(params)
            if len(final_pairs)>0:
                for node,value,ans_piece,attempt_piece in final_pairs:
                    if value>10 or value != int(value):
                        #Update clusters
                        if not node in Reps.keys():
                            Reps[node]=ans_piece
                        Clusters[node]+=1
                        # print hint
                        if node=='R': # attempt is correct
                            sub_type='answer'
                        else:
                            sub_type='sub-expression'
                        if attempt_piece != ans_piece:
                            print 'The %s %s is correct, it could also be written as %s'%(sub_type,attempt_piece,ans_piece)
                        else:
                            print 'The %s %s is correct'%(sub_type,attempt_piece)
                    else:
                        Clusters['Nothing']+=1
            else:
                Clusters['Nothing']+=1


        print 'Clusters='
        print 'Nothing recognizable=',Clusters['Nothing']
        for node in Reps.keys():
            print "%20s%30s%10d"%(node,Reps[node],Clusters[node])
