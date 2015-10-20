### The syntax and semantics of the parse and eval tree.

* The tree is defined recursively, starting with the root. a root consists of a root node descriptor and a list (possibly empty) of trees.

* A node descriptor consists of four elements: 

attempt = `462/2^10`

Tree = `[['/', 0.451171875, [0, 7], 'R'], ['X', 462.0, [0, 2], 'R.0'], [['^', 1024.0, [4, 7], 'R.1'], ['X', 2.0, [4, 4], 'R.1.0'], ['X', 10.0, [6, 7], 'R.1.1']]]`

attempt='(11!/(5!*6!))/2^11'

Tree=[['/', 0.2255859375, [0, 17], 'R'], [['/', 462.0, [1, 11], 'R.0'], [['!', 39916800, [1, 3], 'R.0.0'], ['X', 11.0, [1, 2], 'R.0.0.0']], [['*', 86400.0, [6, 10], 'R.0.1'], [['!', 120, [6, 7], 'R.0.1.0'], ['X', 5.0, [6, 6], 'R.0.1.0.0']], [['!', 720, [9, 10], 'R.0.1.1'], ['X', 6.0, [9, 9], 'R.0.1.1.0']]]], [['^', 2048.0, [14, 17], 'R.1'], ['X', 2.0, [14, 14], 'R.1.0'], ['X', 11.0, [16, 17], 'R.1.1']]]
