#### FindMatchingSubexpression.find_matches(params)

This filter takes as input the dictionary `params` in the same format that is 
recieved by the filter functions.

It finds the subexpressions that match between the correct tree and the attempt tree and returns it as a list of 
tuples, one for each match found. Matches that are sub-expressions of another matched expression are supressed. The
match tuples are of the form (node,value,answer_part,attempt_part), which are:
* `node`: the location in the correct parse tree: `R`=root, `R.0`=first (left) child of root, ..., `R.1.0`= first child of second child of root.
* `value`:  the numerical value of the matching sub-expressions.
* `answer_part`: the string that corresponds to the subexpression in the correct answer.
* `attempt_part`: the string that corresponds to the subexpression in the attempted answer.

**Recommendation:** The most stable way to check what is the correct part is to use the *node* parameter. Other parts 
might vary because of different instances of the same problem might use different setting of the variables. To find 
out which are the most common correct subexpression, use the script FindMatchingSubexpression.py

#### classify_final_value.classify_final_value()

This filter takes as input the dictionary `params` in the same format that is 
recieved by the filter functions.

The output from this file is  a pair: `att_final_value,classification`. `att_final_value` is the number
the number to which the attempt evaluates. `classification` is a list of descriptors that 
apply to the final value associated with the user's attempt. The sossible values in the list are:
* `number/expression` : indicates whether the expression is a single number or an expression (which combines several numbers)
* `correct`: indicates that the attempt is correct (yields the correct value)
* `Inf/not Inf`: indicates whether or not the attempt evaluates to infinity.
* `int/not int`: idicates whether or not the attempt evaluates to an integer number.
