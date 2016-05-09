import pandas as pd
import datetime
import matplotlib.pyplot as pl
from matplotlib.backends.backend_pdf import PdfPages
import datetime
import numpy as np
from pylab import *
from operator import itemgetter

def plot_student_assignment(df,set_id,user_id,part_index,max_gap=30, filename='plot.pdf', legend_pos=2):
    #compute time profile for a single user/assignment

    #compute time-based columns
    df=df.sort(columns='timestamp')
    t=list(df.timestamp)
    df['timefromStart']=[((tt-t[0]).total_seconds()/6)/10. for tt in t]
    df['timediff']=[0.0]+[((t[i+1]-t[i]).total_seconds()/6)/10. for i in range(len(t)-1)]
    df['lags']=[max(0,t-max_gap) for t in df['timediff']]
    td=np.array(df['lags'])
    ts=np.array(df['timefromStart'])
    tn=ts-np.cumsum(td)
    df['adjustedTimeFromStart']=tn


    t=df['timefromStart'].values      # times, with long gaps shrunk to zero
    locs=df['lags'].values            # location and size of long gaps
    t_s=df['adjustedTimeFromStart'].values # times with corrected gap size

    timestamp=list([pd.to_datetime(str(tt))+ datetime.timedelta(0,0,0,0,0,7) for tt in df['timestamp'].values])
    problem_id=df['problem_id'].values
    part_id=df['part_id'].values
    counter=df['part_index'].values # Counter of problem/part
    correct=df['score'].values # whether or not attempt is correct


    tmp1=part_index[set_id]
    part_names=['(%s,%s)'%(prob,part) for ((prob,part),i) in sorted(tmp1.items(), key=itemgetter(1))]

    #    answer=block['answer'].values   # The actual answer?
    # index each trial into one of 6 categories: correct/incorrect, empty/same/different (than previous)
    # according to classification append element into one of 4 lists in a dictionary:
    # "correct/same","correct/different","incorrect/same","incorrect/different"

    Corr=["incorrect","correct"]
    Diff=["!=","=",""]
    _marker={'=':'_','!=':'o','':None}    # define the markers corresponding to same/different/empty
    _color ={'correct':'g','incorrect':'r'}  # define the colors corresponding to correct/incorrect
    _change={"!=":"changed","=":"same","":"empty"}

    # compute sequences for 4 different possible status: 'correct'(True,False) X 'change'(True,False)
    parts=df.groupby('part_index')
    for part_index,part_df in parts:
        answers=part_df['answer_string']
        indices=part_df.index
        for i in range(len(answers)):
            if answers[i]=='': 
                df.loc[indices[i],'change']=''
            else:
                if i==0 or answers[i]!=answers[i-1]:
                    df.loc[indices[i],'change']='!='
                else:
                    #print 'found = for user',user_id,i,answers[i-1],answers[i]
                    df.loc[indices[i],'change']='='

    # prepare time and part arrays for each of the 4 combinations
    time={}; part={}
    for c in Corr: 
        for d in Diff:
            time[(c,d)]=[]; part[(c,d)]=[]

    c=[Corr[int(correct[i])] for i in range(len(correct))]
    d=df['change'].values

    for i in range(len(df.index)):
        time[(c[i],d[i])].append(t_s[i])
        part[(c[i],d[i])].append(counter[i])
    
    #------------------------------------------------------------------------
    # create the scatter plot
    #------------------------------------------------------------------------
    # time, part: tables of lists: indexed by c (Corr) :correct/incorrect and d (Diff): different/same as previous.
    # Each entry is a list: time is a list of times extracted from t_s
    #                       part is the index of the part: extracted from counter[i]

    pp=PdfPages(filename)

    fig=pl.figure(figsize=[10,8])
    max_counter=max(counter)
    pl.ylim((0,max_counter+1))
    center=counter[-1]/2
    minutes = int(t_s[-1]/60)
    pl.xlim((-60,minutes*60+60)) 

    # Put a minute-marking every minutes_delta minutes
    minutes_delta = 10

    pl.xticks(arange(t_s[0],t_s[-1],minutes_delta))
    pl.xlabel('minutes')
    pl.ylabel('part name')
    pl.yticks(range(len(part_names)), part_names)
    # Pad margins so that markers don't get clipped by the axes
    for c in Corr: 
        for d in Diff:
            if len(time[(c,d)])>0:
                pl.scatter(time[(c,d)], part[(c,d)],color=_color[c]\
                           ,marker=_marker[d],label=c+' / '+_change[d])


    #place vertical lines where a time gap has been detected and subtracted.

    def plot_text(x,text):
        pl.text(x, max_counter/2,\
            text,\
            rotation=90,\
            horizontalalignment = 'center',\
            verticalalignment   = 'top',\
            multialignment      = 'center')

    pl.axvline( x=t_s[0],color='b')
    text=timestamp[0].strftime('%a  %H:%M');
    plot_text(t_s[0]-5.0,text)

    for i in range(len(t)-1):
        if locs[i+1]>0:
            # print 'plot at x=',t_s[i]/60,' locs=',locs[i+1]/60
            pl.axvline( x=t_s[i+1],color='b')
            pl.axvline( x=t_s[i],color='r')
            # write the number of minutes elapsed between the two lines.
            # or, if big gap, write time.
            gap=(locs[i+1]+max_gap);
            if gap<120:
                text='rest %4d minutes' % gap;
            else:
                # need to subtract 7 hours
                text=timestamp[i+1].strftime('%a  %H:%M');
            plot_text((t_s[i+1]+t_s[i]+5)/2,text)

    for i in range(len(part_names)):
        if ',1)' in part_names[i]:
            pl.axhline(y=i-0.5,color='k')

    pl.xlim([-10,max(t_s)+5])
    if legend_pos>0: pl.legend(loc=legend_pos)
    pl.title('Attempt times for %s / %s'% (set_id,user_id))
    pp.savefig(fig)

    pp.close()

