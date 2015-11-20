from math import factorial
import linecache
import sys
print string import replace
from webwork_parser import parse_webwork, WebworkParseException, node_string
import traceback
import operator as op
from scipy.stats import norm

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)

def is_number(s):
    try:
        float(s)
        return True
    except:
        return False


def ncr(n, r):
    " compute n choose r "
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer/denom

def npr(n, r):
    " Computer n permute r (order matters)"
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    return numer

def find_common_values(e1,e2):
    """ Find intersection of values in two eval trees.
        If a value is found, all of the values in the subtree below it are ignored.

    returns: common,only_in_1, only_in_2
       Dicts of the form {value: (from,to) } where value is a float.
       
    """
    

def eval_parsed(e, label='R'):
    """ Evaluate a parsed expression, returns a tree, of the same form as the parse tree. Where each operator 
        is replaced by a tuple: (operator,evaluation result)
    
        Still need to write code to handle varibles, lists and sets.
    """
    #print 'in eval_parsed e=|%s|, label=|%s|'%(str(e),str(label))

    def get_number(ev):
        #print 'get_number got',ev
        if len(ev)==4 and ev[0]=='X': 
            return float(ev[1])
        elif len(ev)==1:
            return float(ev[0])
        else: 
            return float(ev[0][1])
        
    try:
        print 'eval_parsed, e="',e,'"'
        if type(e)==type(None):
            return 0
        elif is_number(e)==1:
            return (float(e),)
        elif len(e)==2:
            [[f,span],op]=e

            if f=='{}':
                return [[f,None,span,label],op]  # if element is a list, just return as is.

            ev=eval_parsed(op,label+'.0')
            v=get_number(ev)
            
            if f=='X':  # X indicates a single number
                ans=v
                return [f,ans,span,label]
            elif f=='-':
                ans=-v
            elif f=='!':
                ans=factorial(v)
            elif f=='Q':
                ans= 1-norm.cdf(v)
            else:
                raise Exception('unrecognized unary operator %s in %s'%(f,e))
            return [[f,ans,span,label],ev]
        
        elif len(e)==3:
            [[f,span],op1,op2]=e
            ev1=eval_parsed(op1, label+'.0')
            v1=get_number(ev1)
            ev2=eval_parsed(op2, label+'.1')
            v2=get_number(ev2)

            if f=='+':    ans= v1+v2
            elif f=='*':  ans= v1*v2
            elif f=='-':  ans= v1-v2
            elif f=='/':  ans= v1/v2
            elif f=='**': ans= v1**v2
            elif f=='^': ans= v1**v2
            elif f=='C':
                ans= ncr(int(v1), int(v2))
            elif f=='P':
                ans= npr(int(v1), int(v2))
            else:
                raise Exception('unrecognized binary operator %s in %s'%(f,e))
            return_value=[[f,ans,span,label],ev1,ev2]
            #print 'returned value=',return_value
            return return_value
        else:
            raise Exception('Unrecognized expression form: %s'%e)
    except Exception as ex:
        print 'Eval_parsed Exception:',ex
        #traceback.print_exc()
        traceback.print_exc(file=sys.stdout)
        return None
        #raise WebworkParseException(ex)
        # return ((e[0][0], None, e[0][1]),)


def Collect_numbers(etree):
    T={}
    if type(etree)==int:
        return T
    collection_recursion(T,etree)
    return T

def collection_recursion(T,etree):
    if len(etree)==1:
        T[etree[0]]=etree   # add leaf
    if len(etree)>1:
        T[etree[0][1]]=etree   # add evaluation for non-leaf
        for i in range(1,len(etree)):
            collection_recursion(T,etree[i])

def numbers_and_exps(etree, string):
    numbers = Collect_numbers(etree)
    ret = {k: node_string(v, string) for k, v in numbers.iteritems()}
    return ret

def parse_and_collect_numbers(string):
    try:
        parse_tree, variables = parse_webwork(string)
        if len(variables)==0:
            eval_tree = eval_parsed(parse_tree)
            eval_numbers = Collect_numbers(eval_tree)
            return set(eval_numbers.keys())
        else: 
            return Eval_with_Variables(string,variables)
    except:
        return set()

def Eval_with_Variables(string,variables):

    vars=variables.items();
    tvals=[1,2,3]
    L=len(tvals)
    indexes=[0]*len(variables)
    count=L**len(variables)
    for i in range(count):
        for j in range(L):
            # To Be Continued
            
# def parse_and_eval(string):
#     expr = parse_webwork(string)
#     if expr:
#         try:
#             etree = eval_parsed(expr)
#             return etree
#         except:
#             return None
#     else:
#         return None

if __name__=="__main__":
    string=sys.argv[1]
    print 'input:::',string
    tree,variables=parse_webwork(string)
    print 'output:::',tree, variables
    eval_tree=eval_parsed(tree)
    print 'Eval_tree:::',eval_tree
