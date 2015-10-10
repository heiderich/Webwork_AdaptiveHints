### The parameters passed to the filter
Are in the form of a dictionary, the signature of this dictionary is: `answer_data = {'attempt': answer_string, 'att_tree': etree, 'answer': part_answer,
                        'ans_tree': answer_etree, 'variables':
						user_variables}`
						
Where `attempt` is the string entered by the student. `answer` is the
string representing the answer (after PG variables have been
substituted with their values). `att_tree` is the tree corresponding
to `attempt` and `ans_tree` is the tree corresponding
to `answer`. Finally `user_variables` is a dictionary defining the
value associated with each PG variable.

### The syntax and semantics of the parse and eval tree.

* The tree is defined recursively, starting with the root. a root consists of a root node descriptor and a list (possibly empty) of trees.

* A node descriptor consists of four elements: 
  1. **operator** : the mathematical operation (`+,-,*,/,!,...`) that is taken place between the element. If the node is a leaf (corresponding to a number) then the operator is `X`
  1. **value** : the numerical result of the expression represented by the subtree rooted at the node.
  1. **span** : `[from,to]` Two integers representing the first and the last locations in the expression string corresponding to the subexpression represented by the subtree starting at this node. If the expression string is `attempt` then the part corresponding to the node is `attempt[from:to+1]`
  1. **node_index** : represents the location of this node in the overall tree. The location is represented by a string of the form `R.n.n.n...` where n is a small integer (usually one digit). The root index is `R`, if the root has two childred then their indices are `R.0` and `R.1`, this children of `R.1` are `R.0,R.1,R.2` etc.

Pay attemtion to the representation of the leaves. The leaves are lists of the form 
`['X', 11.0, [1, 2], 'R.0.0.0']`. This is different from a unary expression such as `-6`. Both of these expression would be represented by a tree of depth 2, where the root (`R`) operator is `-` and the single leaf (`R.0`) represents the number `6`.



#### Examples of expressions and their parse tree

attempt = `462/2^10`

Tree = `[['/', 0.451171875, [0, 7], 'R'], ['X', 462.0, [0, 2], 'R.0'], [['^', 1024.0, [4, 7], 'R.1'], ['X', 2.0, [4, 4], 'R.1.0'], ['X', 10.0, [6, 7], 'R.1.1']]]`

attempt=`(11!/(5!*6!))/2^11`

Tree=`[['/', 0.2255859375, [0, 17], 'R'], [['/', 462.0, [1, 11], 'R.0'], [['!', 39916800, [1, 3], 'R.0.0'], ['X', 11.0, [1, 2], 'R.0.0.0']], [['*', 86400.0, [6, 10], 'R.0.1'], [['!', 120, [6, 7], 'R.0.1.0'], ['X', 5.0, [6, 6], 'R.0.1.0.0']], [['!', 720, [9, 10], 'R.0.1.1'], ['X', 6.0, [9, 9], 'R.0.1.1.0']]]], [['^', 2048.0, [14, 17], 'R.1'], ['X', 2.0, [14, 14], 'R.1.0'], ['X', 11.0, [16, 17], 'R.1.1']]]`
