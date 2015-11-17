import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import paramiko

#these parameters need to be set for each TA
IP = "webwork.cse.ucsd.edu"
USERNAME = "yfreund"
set_id='Week5'
ssh_private_key='/Users/yoavfreund/.ssh/id_dsa'

def get_table(set_id):
    """ Connect to database, get _answer_by_part table, parse it, 
    and return it as pandas dataframe"""

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, username='yfreund', key_filename=ssh_private_key)

    command="""mysql -u readonly -preadonly webwork -e 'select *,UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(A.timestamp) as gap
from CSE103_Fall2015_answers_by_part as A 
where A.set_id = "%s" 
    and YEAR(A.timestamp)=2015  
    order by A.timestamp;'
"""%set_id

    # and UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(A.timestamp) < 3600

    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    #ssh_stderr.read()
    data = ssh_stdout.readlines()
    print 'number of lines in response=',len(data)
    line = data[0].strip()
    header = line.split('\t')

    table = []
    for line in data[1:]:
        line=line.strip();
        _id,user_id,answer_id,answer_string,score,problem_id,\
            set_id,part_id,timestamp,gap = line.split('\t')
        problem_id=int(problem_id)
        part_id=int(part_id)
        score=int(score)
        gap=int(gap)+7*3600 # I am consistently getting time stamps that 
                            # are 7 hours in the future, corresponding to GMT, resulting in negative gaps
        
        table.append((_id,user_id,answer_id,answer_string,score,problem_id,set_id,part_id,timestamp,gap))  
    
    df = pd.DataFrame(table,columns=header)
    ssh.close()
    return df    

def total_time_trying(times,maxgap=5):
    """ Compute the total time in a given sequence, 
    where gaps large than maxgap minutes are set to maxgap """
    total=datetime.timedelta()
    max_time=datetime.timedelta(minutes=maxgap)
    t0=datetime.datetime.strptime(times[0],'%Y-%m-%d %H:%M:%S')
    for i in range(1,len(times)):
        t1=datetime.datetime.strptime(times[i],'%Y-%m-%d %H:%M:%S')
        gap=t1-t0
        if gap>max_time:
            #print 'clipped',str(gap)
            gap=max_time
        #else:
        #    print str(gap),
        total+=gap
        t0=t1
    return total,len(times)


ranges=(('10 min',600),('1 hour',3600),('10 hours',36000),('anything',1000000))
def calc_gaps(gap_trace):
    """ Given a list of times, return a list of counts according to ranges of times in the past """
    t1=-1000000
    answer=[]
    for name,t2 in ranges:
        answer.append(sum((gaps>=t1)&(gaps<t2)))
        t1=t2
    return answer

if __name__=='__main__':

    df=get_table(set_id)
    A=df.groupby(['problem_id','part_id','user_id'])
    
    Summary={}
    for name,group in A:
        problem,part,ID=name
        success=(sum(group['score']) >0)
        key=(problem,part,success);
        if not key in Summary.keys():
            Summary[key]={'time':0,'tries':0,'students':0}
        Summary[key]['students']+=1    
        T,L=total_time_trying(list(group['timestamp']))
        Summary[key]['tries']+=L
        Summary[key]['time']+=T.seconds
        
    Comb_Summary={}
    #Combine successful and unsuccsessful for each problem and part
    for key in Summary.keys():
        if not key[:2] in Comb_Summary.keys():
            Comb_Summary[key[:2]]={}
        Comb_Summary[key[:2]][key[2]]=Summary[key]

    print 'Summary for %s, at time=%s '%(set_id,str(datetime.datetime.now()))
    print 'problem\t part \t\t FAILURE \t\t SUCCESS'
    print '\t\t  stud\t time\t tries\t  stud\t time\t tries'
    for key in sorted(Comb_Summary.keys()):
        row=Comb_Summary[key]
        print "%2d\t%2d"%key,
        for x in [False,True]:
            if not x in row.keys():
                row[x]={'students': 0.01, 'time': 0, 'tries': 0}
            row[x]['aver_time']=float(row[x]['time'])/row[x]['students']
            row[x]['aver_tries']=float(row[x]['tries'])/row[x]['students']                                                    
                                                        
            print '\t%5.0f\t%5.2f\t%5.2f'%\
                (row[x]['students'],row[x]['aver_time'],row[x]['aver_tries']),
        print

