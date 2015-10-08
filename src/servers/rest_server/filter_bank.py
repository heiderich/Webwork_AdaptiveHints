"""
This module is responsible for managing and executing the filters used in the adaptive hints System
"""
import logging
logger = logging.getLogger(__name__)

import sys
import glob
import string
import json
import traceback
from TimeoutError import timeout # a decorator that creates a time-out interrupt for a given function.
import StringIO
import inspect

class filter_bank:
    def __init__(self):
       """self.env is the environment that contains all of he filter
       functions and within which the filters are executed.
       """
       self.env={}

    def get_env_keys(self):
        return self.env.keys()

    def import_filters_from_files(self,filter_dir):
        for filename in glob.glob(filter_dir+'*.py'):
            filtername=filename[len(filter_dir):-3]
            code=open(filename,'r').read()
            self.add_filter(filtername,code)
        return self.get_env_keys()

    def get_docstring(self,filter_name):
        if self.env.has_key(filter_name):
            return self.env[filter_name].__doc__
        else:
            return 'no filter named '+filter_name

    def get_code(self, filter_dir, filter_name):
        if self.env.has_key(filter_name):
            with open(filter_dir+filter_name+".py", 'r') as f:
                f.readline()
                return f.read()
        else:
            return 'no filter named '+filter_name
    
    def add_filter(self,name,code,replace=False):
        '''
        make_filter takes a function source string as input and returns a pointer to the executable function

        parameters:
           code: a string containing the code of the function
           name: the name of the function (has to be consistent with the code)
           replace: a flag indicating whether to overwrite a filter with the same name (default=False)

        return value:
           if None: function added successfully
           if string: the string is an error message
        '''

        if self.env.has_key(name):
            if replace:
                old_filter=self.env.pop(name)
            else:
                return 'Filter named: %s already exists, set "replace=True"'%name

        message='';
        try:
            bytecode=compile(source=code,filename='filter source code',mode='exec')

            exec(bytecode,self.env) # running this bytecode creates the function, it does not run it.

        except SyntaxError, e:
            message='Syntax error:\n'
            message+= 'line %5d:%s'%(e.lineno,e.text)
            message+= ' '*10+'-'*e.offset+'^'
            
        if self.env.has_key(name):   # success
            return None
        else:
            if 'old_filter' in locals():  # if filter generation failed - put back in the old filter (if it existed)
                self.env[name]=old_filter
                return 'code failed to generate new function named '+name+'old definition retained\n'+message
            else:
                return 'code failed to generate function named '+name+'\n'+message

    def exec_filter(self,filtername,input):
        """ execute a filter on a given input.

        params:
            filtername:  the name of the filter (a string)
            input: the input to the filter (a tuple containing all parameters)

        returns:   status, hint/error, stdout

                status indicates whether or not execution succeeded
                if status = True then second element is the hint (empty if no match)
                if status = False then second element is the error message (caught exception)
                stdout is what the filter "print"s during execution.
        """
        self.env['input']=input
        command='out=%s(input)'%filtername

        if self.env.has_key('out'):
            self.env.pop('out')

        logger.debug('before executing '+command)
        logger.debug('input= '+str(input))
        logger.debug('env_keys= '+str(self.env.keys()))

        old_stdout=sys.stdout
        sys.stdout=StringIO.StringIO()

        try:  # exception should go just over exec and should generate a complete traceback in case of error
            self.__exec__(command)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            stdout_dump=sys.stdout.getvalue()
            error_message=traceback.format_exc()
            #logger.error('Runtime Error in Filter:'+error_message)
        finally:
            stdout_dump=sys.stdout.getvalue()
            sys.stdout=old_stdout

        logger.debug('after executing '+command)
        logger.debug('env_keys='+str(self.env.keys()))
        logger.debug('stdout='+stdout_dump)

        if self.env.has_key('out'):
            return True,self.env.pop('out'),stdout_dump
        else:
            return False,error_message,stdout_dump

    @timeout(1)  # does not support less than 1 sec
    def __exec__(self,command):
        exec(command,self.env)

if __name__=="__main__": 
    """ Testing filter_bank """

    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler()) # direct logs to stderr

    filters=filter_bank()

    print filters.import_filters_from_files('filter_helpers/')
    print filters.import_filters_from_files('filters/')

    for filtername in ['answer_should_be_int', 'answer_is_not_expression', 'flatten']:
        print filters.get_docstring(filtername)


    ###
    # testing adding filters with different errors in the code
    ###

    #the common part of the code defining the filter
    common_code="""def answer_filter(params):
    import json
    print json.dumps(params)
    %s
    return 'this is a hint'
    """

    filtername='answer_filter'

    # Lines that are inserted into the code (at the %s location)
    # That test various error conditions.

    error_lines={'none':"",
                 'syntax error':"x=1:",
                 'runtime error':"x+=1",
                 'runtime misreference':"print params[3]",
                 'termination error':"while True: x=1"
    }

    # Representative input lines that define the parameters to the filter in json format
    input_lines={'good line':'["22/36", [["/", [0, 3]], 22, 36], [["/", 0.6111111111111112, [0, 3]], [22.0], [36.0]], "", null, 0, {"$n2": 3.0}]',
                 'bad_line':'[1,2]'}

    for error_type in error_lines.keys():
        code=common_code%error_lines[error_type]
        print '-'*50
        print 'error type='+error_type
        print 'code=\n'+code
        status=filters.add_filter(filtername,code,replace=True)
        if status==None:
            print 'compiled the filter successfully'
        else:
            print 'error creating the filter',status
            continue

        #print 'Current env keys = ',filters.get_env_keys()

        answer=json.loads(input_lines['good line'])
        for input_type in input_lines.keys():
            input=input_lines[input_type]
            print '='*20
            print "input params=",input
            params=json.loads(input);
            status,hint,output = filters.exec_filter(filtername,params)
            print 'code=%s, input=%s, Status='%(error_type,input_type),status
            print 'return value=\n',hint
            print 'stdout=\n',output,

