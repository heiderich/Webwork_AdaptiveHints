def correct_answer(params):
    """ Written by Yoav Freund, Tue Oct 13 17:14:01 PDT 2015
    Check whether the attempt is correct, returns True if correct, False otherwise
    """

    att_tree=params['att_tree']
    att_final_value=att_tree[0][1]
    ans_tree=params['ans_tree']
    ans_final_value=ans_tree[0][1]

    return att_final_value == ans_final_value
    
