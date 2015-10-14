def classify_final_value(params):
    """ Written by Yoav Freund, Sat Sep 19 17:09:48 PDT 2015
    classifies the final value as: correct,inf, int, not_int
    """
    att_tree=params['att_tree']
    att_final_value=att_tree[0][1]
    ans_tree=params['ans_tree']
    ans_final_value=ans_tree[0][1]
    
    if att_final_value==ans_final_value:
        return 'correct'
    if isinf(att_final_value):
        return "inf"
    if int(att_final_value)!=att_final_value:
        return "not int"
    else:
        return "int"
