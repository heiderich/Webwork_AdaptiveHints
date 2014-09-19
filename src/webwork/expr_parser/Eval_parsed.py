from math import factorial
import linecache
import sys

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

def eval_parsed(e):
    """ Evaluate a parsed expression, returns a tree, of the same form as the parse tree. Where each operator 
        is replaced by a binary tuple: (operator,evaluation result)
    
        Still need to write code to handle varibles, lists and sets.
    """
    def get_number(ev):
        if len(ev)==1: return ev[0]
        else: return ev[0][1]
        
    try:
        if is_number(e)==1:
            return (float(e),)
        elif len(e)==2:
            ((f,span),op)=e
            ev=eval_parsed(op)
            v=get_number(ev)
            
            if f=='-':
                ans=-v
            elif f=='!':
                ans=factorial(v)
            else:
                raise Exception('unrecognized unary operator',f,'in',e)
            return ((f,ans,span),ev)
        
        elif len(e)==3:
            ((f,span),op1,op2)=e
            ev1=eval_parsed(op1)
            v1=get_number(ev1)
            ev2=eval_parsed(op2) 
            v2=get_number(ev2)
            
            if f=='+':    ans= v1+v2
            elif f=='*':  ans= v1*v2
            elif f=='-':  ans= v1-v2
            elif f=='/':  ans= v1/v2
            elif f=='**': ans= v1**v2
            elif f=='C':  ans= factorial(v1)/(factorial(v2)*factorial(v1-v2))
            else:
                raise Exception('unrecognized binary operator',f,'in',e)
            return ((f,ans,span),ev1,ev2)
        else:
            raise Exception('Unrecognized expression form:',e)
    except Exception as ex:
        PrintException()
        
def Collect_numbers(etree):
    T={}
    collection_recursion(T,etree)
    return T

def collection_recursion(T,etree):
    if len(etree)==1:
        T[etree[0]]=etree   # add leaf
    if len(etree)>1:
        T[etree[0][1]]=etree   # add evaluation for non-leaf
        for i in range(1,len(etree)):
            collection_recursion(T,etree[i])
            
    