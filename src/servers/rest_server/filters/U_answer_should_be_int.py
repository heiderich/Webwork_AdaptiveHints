def U_answer_should_be_int(params):
    """Written by Yoav Freund, Sat Sep 19 17:09:48 PDT 2015
    Assumes answer should be an integer number, send a hint if not
    """
    #{'string': '', 'correct_eval': None, 'correct_tree': []], 'evaled': None, 'correct_string': '', 'parsed': []}
    eval_tree = params['evaled']
    if eval_tree == None:
        return ""
    if len(eval_tree)==1:
        final_value=eval_tree[0]
    elif len(eval_tree)>1:
        final_value=eval_tree[0][1]
    else:
        final_value=0
    if int(final_value)!=final_value:
        return "Can the answer to this question be a fractional number?(y,n)  [__]{'n'}"
    else:
        return ""