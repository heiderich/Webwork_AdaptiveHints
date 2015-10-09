def U_answer_is_not_expression(params):
    #{'attempt': answer_string, 'attemp_tree': ptree, 'answer': part_answer, 'answer_tree': answer_ptree, 'variables': user_variables}
    if params['evaled'] == None:
    	return ""
    if len(params['evaled'])==1:
        return "Please enter an expression, not just final numerical result"
    else:
        return ""