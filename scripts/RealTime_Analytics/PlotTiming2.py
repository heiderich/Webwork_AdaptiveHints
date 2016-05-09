#!/usr/bin/env python

"""Yoav: I took this code written by Matt Elkherj and am extracting
from it just the part that generates the plots. Removing the parts 
that reads in and parses the data and handle multiple graphs.
"""

import pandas, sys,os
import numpy as np
import pickle
import matplotlib.pyplot as pl
from matplotlib.backends.backend_pdf import PdfPages


"""generate plots describing the time sequence of answers for a
    user/assignment.

    """
# def __init__(self,filename):
#     print 'starting to load',filename
#     Dict=pickle.load(open(filename,'rb'))
#     self.__dict__=Dict
#     print 'finished loading, loaded',self.__dict__.keys()

def plot(df,filename='plots.pdf',legend=2):
    """
    create a plot file for a (user,assignment) pair.
    df = a dataframe holding the information extracted from the webwork database.
    filename = the name of the pdf file in which the plots are stored.
    legend = location of the legend (0=none, 1=upper right, 2=(default) upper left, 3=lower left, 4=lower right)
    """
    pp=PdfPages(filename)

    last_answer={}

    t=block['time'].values      # times, with long gaps shrunk to zero
    locs=block['break'].values  # location and size of long gaps
    steps=np.cumsum(np.array([(self.time_gap_threshold if l>0 else 0) for l in locs]))
    t_s=t+steps                 # times with fixed gap size

    counter=block['counter'].values # Counter of problem/part
    correct=block['correct'].values # whether or not attempt is correct
#    answer=block['answer'].values   # The actual answer?

    # index each trial into one of 6 categories: correct/incorrect, empty/same/different (than previous)
    # according to classification append element into one of 4 lists in a dictionary:
    # "correct/same","correct/different","incorrect/same","incorrect/different"

    Corr=["incorrect","correct"]
    Diff=["=","!=",""]
    _marker={'=':'_','!=':'o','':None}    # define the markers corresponding to same/different/empty
    _color ={'correct':'g','incorrect':'r'}  # define the colors corresponding to correct/incorrect

    # prepare time and part arrays for each of the 4 combinations
    time={}; part={}
    for c in Corr: 
        for d in Diff:
            time[(c,d)]=[]; part[(c,d)]=[]

    answer_state=block['answer_state'].values
    c=[Corr[int(correct[i])] for i in range(len(correct))]

    for i in range(len(block.index)):
        time[(c[i],answer_state[i])].append(t_s[i])
        part[(c[i],answer_state[i])].append(counter[i])

    #---------------------------
    # create the scatter plot
    # time, part: tables of lists: indexed by c (Corr) :correct/incorrect and d (Diff): different/same as previous.
    # Each entry is a list: time is a list of times extracted from t_s
    #                       part is the index of the part: extracted from counter[i]

    fig=pl.figure(figsize=[15,10])
    max_counter=max(counter)
    pl.ylim((0,max_counter+1))
    center=counter[-1]/2
    minutes = int(t_s[-1]/60)
    pl.xlim((-60,minutes*60+60)) 
    # Put a minute-marking every minutes_delta minutes
    minutes_delta = 10
    pl.xticks(range(0,minutes*60,minutes_delta*60),\
              range(0,minutes,minutes_delta))
    pl.xlabel('minutes')
    pl.ylabel('part number')
    for c in Corr: 
        for d in Diff:
            if len(time[(c,d)])>0:
                pl.scatter(time[(c,d)], part[(c,d)],color=_color[c]\
                           ,marker=_marker[d],label=c+'/'+d)

    #place vertical lines where a time gap has been detected and subtracted.
    for i in range(len(t)-1):
        if locs[i+1]>0:
            # print 'plot at x=',t_s[i]/60,' locs=',locs[i+1]/60
            pl.axvline( x=t_s[i+1],color='b')
            pl.axvline( x=t_s[i]+60,color='r')
            # write the number of minutes elapsed between the two lines.
            pl.text((t_s[i+1]+t_s[i]+5)/2, max_counter/2,\
                     ('rest of %4d minutes' % (locs[i+1]/60)),\
                     rotation='vertical',\
                     horizontalalignment = 'center',\
                     verticalalignment   = 'top',\
                     multialignment      = 'center')

    if legend>0: pl.legend(loc=legend)
    pl.title('Attempt times for %s / %s'% key)
    pp.savefig(fig)

    pp.close()


if __name__=='__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Create timing plots from log files')
    parser.add_argument('-a','--assignment', default='',
                        help='restrict to a specific assignment (default = no restriction)')
    parser.add_argument('-s','--student', default='',
                        help='restrict to a specific student (default = no restriction)')

    args = vars(parser.parse_args())
    output_file=args['student']+'.'+args['assignment']+'.pdf'
    
    if 'WWAH_PICKLE' in os.environ.keys() and 'WWAH_OUTPUT' in os.environ.keys():
        pickle_dir=os.environ['WWAH_PICKLE']
        output_dir=os.environ['WWAH_OUTPUT']
        P=PlotTiming(pickle_dir+'/ProcessedLogs.pkl')
        filename=os.path.join(output_dir,output_file)
        P.plot(user=args['student'], assignment=args['assignment'],filename=filename)
        print 'output file is ',filename
    else:
        print 'source setup.sh first'
