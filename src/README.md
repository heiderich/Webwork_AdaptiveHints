# Source Code #

### \clients ---> front-end code ###
- **/teacher_client**
	- front-end code for adaptive hints interface
- **/webwork_js**
	- js file to keep track of students' answers and send hints lives

### \servers ---> back-end code ###
- **/init-scripts**	
	- used to initialize service for local development environemnt
- **/rest_server**
	- REST API with a README.md inside folder
- **/sockjs_server**
	- contains files for sockjs server and a README.md inside folder
- **/hint_filters**
- **/nagios_plugins**
	- Connects the application to Nagios which is a system monitoring software. I (yoav) regularly get email messages from Nagios when the system is overloaded.
	

### \parsetrees ---> a python module for parsing and comparing expressions ###
- **/expr_parser**
	- contains python modules to parse expression
- **/zhang_sasha**
	- contains code for Zhang-Shasha Algorithm
	- Zhang-Shasha Algorithm is used to compute tree edit distance
- **/oneoffs**
- **/test**

### \databases ---> scripts to manage database tables

### \old ---> contains old code for adaptive hints front-end and back-end ###