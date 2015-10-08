### 1. CSE103_Fall2015_achievement
***Description***:

description1

***Schema***:
```
  | Field          | Type     | Null | Key | Default | Extra
--|----------------|----------|------|-----|---------|------
0 | achievement_id | tinyblob | NO   | PRI | None    |      
1 | name           | text     | YES  |     | None    |      
2 | description    | text     | YES  |     | None    |      
3 | points         | int(11)  | YES  |     | None    |      
4 | test           | text     | YES  |     | None    |      
5 | icon           | text     | YES  |     | None    |      
6 | category       | text     | YES  |     | None    |      
7 | enabled        | int(11)  | YES  |     | None    |      
8 | max_counter    | int(11)  | YES  |     | None    |      
```
***Example***:
```
This table is empty!
```
--------------------------------------------------
### 2. CSE103_Fall2015_achievement_user
***Description***:

description2

***Schema***:
```
  | Field          | Type          | Null | Key | Default | Extra
--|----------------|---------------|------|-----|---------|------
0 | user_id        | tinyblob      | NO   | PRI | None    |      
1 | achievement_id | tinyblob      | NO   | PRI | None    |      
2 | earned         | int(11)       | YES  |     | None    |      
3 | counter        | int(11)       | YES  |     | None    |      
4 | frozen_hash    | varchar(1024) | YES  |     | None    |      
```
***Example***:
```
This table is empty!
```
--------------------------------------------------
### 3. CSE103_Fall2015_answers_by_part
***Description***:

description3

***Schema***:
```
  | Field         | Type          | Null | Key | Default | Extra         
--|---------------|---------------|------|-----|---------|---------------
0 | id            | int(11)       | NO   | PRI | None    | auto_increment
1 | user_id       | varchar(100)  | NO   | MUL | None    |               
2 | answer_id     | int(11)       | NO   |     | None    |               
3 | answer_string | varchar(1024) | YES  |     | None    |               
4 | score         | varchar(1)    | NO   |     | None    |               
5 | problem_id    | int(11)       | NO   | MUL | None    |               
6 | set_id        | varchar(100)  | NO   | MUL | None    |               
7 | part_id       | int(11)       | NO   |     | None    |               
8 | timestamp     | datetime      | NO   |     | None    |               
```
***Example***:
```
     | answer_id | answer_string | id   | part_id | problem_id | score | set_id      | timestamp           | user_id 
-----|-----------|---------------|------|---------|------------|-------|-------------|---------------------|---------
744  | 322       | D             | 745  | 4       | 14         | 1     | Orientation | 2013-09-28 00:07:07 | thk002  
534  | 269       | B             | 535  | 3       | 13         | 1     | Orientation | 2013-09-27 23:52:42 | mabid   
245  | 843       | 1             | 246  | 1       | 11         | 0     | Orientation | 2013-09-28 21:22:29 | whyao   
1907 | 344       | cos(5x)       | 1908 | 1       | 8          | 1     | Orientation | 2013-09-28 00:24:05 | ercrawfo
1358 | 154       | x^3           | 1359 | 1       | 5          | 1     | Orientation | 2013-09-27 21:26:20 | a5taylor
```
--------------------------------------------------
### 4. CSE103_Fall2015_assigned_hint
***Description***:

description4

***Schema***:
```
  | Field      | Type         | Null | Key | Default           | Extra                      
--|------------|--------------|------|-----|-------------------|----------------------------
0 | id         | int(11)      | NO   | PRI | None              | auto_increment             
1 | set_id     | varchar(255) | NO   |     | None              |                            
2 | problem_id | int(11)      | NO   |     | None              |                            
3 | pg_id      | varchar(255) | NO   |     | None              |                            
4 | user_id    | varchar(255) | NO   |     | None              |                            
5 | hint_id    | int(11)      | NO   | MUL | None              |                            
6 | assigned   | timestamp    | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP
7 | hint_html  | text         | NO   |     | None              |                            
```
***Example***:
```
  | assigned            | hint_html | hint_id | id | pg_id | problem_id | set_id                     | user_id 
--|---------------------|-----------|---------|----|-------|------------|----------------------------|---------
0 | 2015-09-28 16:23:07 |           | 1       | 1  | a     | 1          | compoundProblemExperiments | melkherj
1 | 2015-09-28 16:23:07 |           | 2       | 2  | b     | 1          | compoundProblemExperiments | melkherj
```
--------------------------------------------------
### 5. CSE103_Fall2015_assigned_hint_feedback
***Description***:

description5

***Schema***:
```
  | Field            | Type         | Null | Key | Default           | Extra                      
--|------------------|--------------|------|-----|-------------------|----------------------------
0 | assigned_hint_id | int(11)      | NO   | MUL | None              |                            
1 | feedback         | varchar(255) | NO   |     | None              |                            
2 | timestamp        | timestamp    | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP
```
***Example***:
```
This table is empty!
```
--------------------------------------------------
### 6. CSE103_Fall2015_assigned_hint_filter
***Description***:

description6

***Schema***:
```
  | Field          | Type      | Null | Key | Default           | Extra                      
--|----------------|-----------|------|-----|-------------------|----------------------------
0 | hint_id        | int(11)   | NO   | PRI | None              |                            
1 | hint_filter_id | int(11)   | NO   | PRI | None              |                            
2 | assigned       | timestamp | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP
3 | trigger_cond   | text      | YES  |     | None              |                            
```
***Example***:
```
This table is empty!
```
--------------------------------------------------
### 7. CSE103_Fall2015_correct_answers
***Description***:

description7

***Schema***:
```
  | Field      | Type         | Null | Key | Default | Extra
--|------------|--------------|------|-----|---------|------
0 | set_id     | varchar(255) | NO   | MUL | None    |      
1 | problem_id | int(11)      | NO   | MUL | None    |      
2 | user_id    | varchar(255) | NO   | MUL | None    |      
3 | part_id    | int(11)      | NO   | MUL | None    |      
4 | answer     | text         | YES  |     | None    |      
```
***Example***:
```
     | answer          | part_id | problem_id | set_id | user_id 
-----|-----------------|---------|------------|--------|---------
163  | {3,5,7,9,11,13} | 2       | 1          | Week2  | rshroyer
1070 | {1}             | 2       | 2          | Week2  | nisharma
1336 | {0}             | 1       | 2          | Week2  | xil109  
1791 | {0,5}           | 1       | 3          | Week2  | wej001  
1494 | {0,2,3}         | 3       | 2          | Week2  | nhn018  
```
--------------------------------------------------
### 8. CSE103_Fall2015_global_user_achievement
***Description***:

description8

***Schema***:
```
  | Field                | Type          | Null | Key | Default | Extra
--|----------------------|---------------|------|-----|---------|------
0 | user_id              | tinyblob      | NO   | PRI | None    |      
1 | achievement_points   | int(11)       | YES  |     | None    |      
2 | next_level_points    | int(11)       | YES  |     | None    |      
3 | level_achievement_id | varchar(100)  | YES  |     | None    |      
4 | frozen_hash          | varchar(1024) | YES  |     | None    |      
5 | facebooker           | int(11)       | YES  |     | None    |      
```
***Example***:
```
    | achievement_points | facebooker | frozen_hash                                        | level_achievement_id | next_level_points | user_id 
----|--------------------|------------|----------------------------------------------------|----------------------|-------------------|---------
380 | 170                | None       | 	   ‚   completeSets¢   completeProblems    | None                 | None              | ksmurlo 
68  | 870                | None       |    –   completeSets
174   completeProblems | None                 | None              | cjy008  
174 | 70                 | None       |       completeSetsŽ   completeProblems    | None                 | None              | amahrous
210 | 170                | None       | 	   ¢   completeProblems‚   completeSets    | None                 | None              | asetters
54  | 1010               | None       |    —   completeSets
202   completeProblems | None                 | None              | kegu    
```
--------------------------------------------------
### 9. CSE103_Fall2015_hint
***Description***:

description9

***Schema***:
```
  | Field      | Type         | Null | Key | Default           | Extra                      
--|------------|--------------|------|-----|-------------------|----------------------------
0 | id         | int(11)      | NO   | PRI | None              | auto_increment             
1 | pg_text    | mediumtext   | NO   |     | None              |                            
2 | author     | varchar(255) | NO   |     | None              |                            
3 | set_id     | varchar(255) | NO   |     | None              |                            
4 | problem_id | int(11)      | NO   |     | None              |                            
5 | part_id    | int(11)      | YES  |     | None              |                            
6 | created    | timestamp    | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP
7 | deleted    | tinyint(1)   | YES  |     | 0                 |                            
```
***Example***:
```
  | author   | created             | deleted | id | part_id | pg_text                                  | problem_id | set_id
--|----------|---------------------|---------|----|---------|------------------------------------------|------------|-------
0 | melkherj | 2015-09-28 16:23:07 | 0       | 1  | None    | This might help: what is 1+1?  [____]{2} | 0          |       
1 | melkherj | 2015-09-28 16:23:07 | 0       | 2  | None    | This might help: what is 2+2?  [____]{4} | 0          |       
```
--------------------------------------------------
### 10. CSE103_Fall2015_hint_filter
***Description***:

description

***Schema***:
```
  | Field       | Type         | Null | Key | Default | Extra         
--|-------------|--------------|------|-----|---------|---------------
0 | id          | int(11)      | NO   | PRI | None    | auto_increment
1 | filter_name | varchar(255) | NO   |     | None    |               
```
***Example***:
```
This table is empty!
```
--------------------------------------------------
### 11. CSE103_Fall2015_key
***Description***:

description

***Schema***:
```
  | Field             | Type       | Null | Key | Default | Extra
--|-------------------|------------|------|-----|---------|------
0 | user_id           | tinyblob   | NO   | PRI | None    |      
1 | key_not_a_keyword | text       | YES  |     | None    |      
2 | timestamp         | bigint(20) | YES  |     | None    |      
```
***Example***:
```
    | key_not_a_keyword                | timestamp  | user_id 
----|----------------------------------|------------|---------
261 | sD72tD36PD7g8bbNpHQ9L7cv6Ufc6vbN | 1443903520 | jic212  
99  | Gh97lTCJnKCTMxjcLhJibCImi5npWDlF | 1386613397 | calmajos
442 | LiILSh5NnlH3v6kepS8lGNDSZERZ5AQC | 1444076763 | aordookh
413 | VwSK0U5kQoO2MqPnVVnES0oklyMrXHIG | 1443996018 | csl030  
200 | F7tLNUyJkthCQoSc2I1TWOSg7iyR7NO3 | 1386379987 | fake    
```
--------------------------------------------------
### 12. CSE103_Fall2015_password
***Description***:

description

***Schema***:
```
  | Field    | Type     | Null | Key | Default | Extra
--|----------|----------|------|-----|---------|------
0 | user_id  | tinyblob | NO   | PRI | None    |      
1 | password | text     | YES  |     | None    |      
```
***Example***:
```
    | password                                                                                                   | user_id 
----|------------------------------------------------------------------------------------------------------------|---------
542 | $6$5I43PTztqU8NRVVy$GJM964XK2ZHkpx6QEJIvIiC0xJXjatXZ6AD4EeS7OPct4sQF0yx0lQBy6q5bdY9w0Fxre01NBRq5GrBrm9.O3/ | xiw230  
193 | KDhs6iY3dpHR6                                                                                              | rvillanu
415 | $6$.SjiMFGIqBTACK9f$K3BI4stlz9aUCaC.2SSUBsB.KQOsyzyo2.MBvPbO.xmx0p1ej33EHUMTcTE3wzcTsZnLXvlHY1s7yCbclhoeo/ | dis003  
474 | $6$PjkOyqiuudUu2eH0$cuaZrk/QsRExqSwJhi6u05Uiw6tj6r8mC7Tan3sneKZLSCqwxan8F1HkdC87e5iVx6pw5I9y8/YLrDBO/qMQ00 | rloza   
67  | Uhnzi4DAyBlq.                                                                                              | d8kwon  
```
--------------------------------------------------
### 13. CSE103_Fall2015_past_answer
***Description***:

description

***Schema***:
```
  | Field          | Type          | Null | Key | Default | Extra         
--|----------------|---------------|------|-----|---------|---------------
0 | answer_id      | int(11)       | NO   | PRI | None    | auto_increment
1 | course_id      | varchar(100)  | NO   | PRI | None    |               
2 | user_id        | varchar(100)  | NO   | PRI | None    |               
3 | set_id         | varchar(100)  | NO   | PRI | None    |               
4 | problem_id     | varchar(100)  | NO   | PRI | None    |               
5 | source_file    | text          | YES  |     | None    |               
6 | timestamp      | int(11)       | YES  |     | None    |               
7 | scores         | tinytext      | YES  |     | None    |               
8 | answer_string  | varchar(1024) | YES  |     | None    |               
9 | comment_string | varchar(1024) | YES  |     | None    |               
```
***Example***:
```
    | answer_id | answer_string                                              | comment_string | course_id   | problem_id | scores  | set_id      | source_file              | timestamp  | user_id 
----|-----------|------------------------------------------------------------|----------------|-------------|------------|---------|-------------|--------------------------|------------|---------
32  | 33        | cos(pi)	1/tan(x)	arcsin(t+1)	[sin(x)-cos(x)]/[sqrt(2x-7)]	 | None           | UCSD_CSE103 | 7          | 1111    | Orientation | setOrientation/prob07.pg | 1380315811 | jagustin
774 | 775       | -11	7+9	18-2	32/2	4*4	8*2	4(30-5)	                         | None           | UCSD_CSE103 | 3          | 1111111 | Orientation | setOrientation/prob03.pg | 1380395569 | rqiu    
921 | 922       | cos5x				                                                  | None           | UCSD_CSE103 | 8          | 0000    | Orientation | setOrientation/prob08.pg | 1380410862 | holi    
473 | 474       | 32	0.67	20	65	128	                                         | None           | UCSD_CSE103 | 4          | 10111   | Orientation | setOrientation/prob04.pg | 1380344979 | tiw005  
614 | 615       | (-1,0)	<-3,1,-5>	<-1,4,2> + <0,2,1>	                       | None           | UCSD_CSE103 | 10         | 111     | Orientation | setOrientation/prob10.pg | 1380360034 | dnl001  
```
--------------------------------------------------
### 14. CSE103_Fall2015_permission
***Description***:

description

***Schema***:
```
  | Field      | Type     | Null | Key | Default | Extra
--|------------|----------|------|-----|---------|------
0 | user_id    | tinyblob | NO   | PRI | None    |      
1 | permission | int(11)  | YES  |     | None    |      
```
***Example***:
```
    | permission | user_id 
----|------------|---------
222 | 0          | hmangalo
22  | 0          | rchaloux
257 | 0          | masaro  
4   | 0          | z3meng  
511 | 0          | megoel  
```
--------------------------------------------------
### 15. CSE103_Fall2015_problem
***Description***:

description

***Schema***:
```
  | Field              | Type     | Null | Key | Default | Extra
--|--------------------|----------|------|-----|---------|------
0 | set_id             | tinyblob | NO   | PRI | None    |      
1 | problem_id         | int(11)  | NO   | PRI | None    |      
2 | source_file        | text     | YES  |     | None    |      
3 | value              | int(11)  | YES  |     | None    |      
4 | max_attempts       | int(11)  | YES  |     | None    |      
5 | flags              | text     | YES  |     | None    |      
6 | showMeAnotherCount | int(11)  | YES  |     | None    |      
7 | showMeAnother      | int(11)  | YES  |     | None    |      
```
***Example***:
```
    | flags | max_attempts | problem_id | set_id         | showMeAnother | showMeAnotherCount | source_file                                                  | value
----|-------|--------------|------------|----------------|---------------|--------------------|--------------------------------------------------------------|------
13  | None  | -1           | 2          | Week5          | nan           | nan                | Reorganized/ConditionalProbability/ConditionalProbability.pg | 1    
10  | None  | -1           | 3          | BasicExamples  | nan           | nan                | local/setBasicExamples/event_tree_3.pg                       | 1    
116 | None  | -1           | 39         | UnusedProblems | nan           | nan                | Reorganized/ExpectationVariance/Notes3_5_3.pg                | 1    
118 | None  | -1           | 41         | UnusedProblems | nan           | nan                | Reorganized/Covariance/ContingencyTables7.pg                 | 1    
255 | None  | -1           | 19         | Week1          | nan           | nan                | Reorganized/EventSpace/event_tree_4.pg                       | 1    
```
--------------------------------------------------
### 16. CSE103_Fall2015_problem_user
***Description***:

description

***Schema***:
```
   | Field              | Type     | Null | Key | Default | Extra
---|--------------------|----------|------|-----|---------|------
0  | user_id            | tinyblob | NO   | PRI | None    |      
1  | set_id             | tinyblob | NO   | PRI | None    |      
2  | problem_id         | int(11)  | NO   | PRI | None    |      
3  | source_file        | text     | YES  |     | None    |      
4  | value              | int(11)  | YES  |     | None    |      
5  | max_attempts       | int(11)  | YES  |     | None    |      
6  | problem_seed       | int(11)  | YES  |     | None    |      
7  | status             | float    | YES  |     | None    |      
8  | attempted          | int(11)  | YES  |     | None    |      
9  | last_answer        | text     | YES  |     | None    |      
10 | num_correct        | int(11)  | YES  |     | None    |      
11 | num_incorrect      | int(11)  | YES  |     | None    |      
12 | sub_status         | float    | YES  |     | None    |      
13 | flags              | text     | YES  |     | None    |      
14 | showMeAnotherCount | int(11)  | YES  |     | None    |      
15 | showMeAnother      | int(11)  | YES  |     | None    |      
```
***Example***:
```
     | attempted | flags | last_answer | max_attempts | num_correct | num_incorrect | problem_id | problem_seed | set_id         | showMeAnother | showMeAnotherCount | source_file | status | sub_status | user_id   | value
-----|-----------|-------|-------------|--------------|-------------|---------------|------------|--------------|----------------|---------------|--------------------|-------------|--------|------------|-----------|------
843  | 0         | None  | None        | None         | 0           | 0             | 5          | 2211         | Week1          | None          | None               | None        | 0.0    | 0.0        | ajudah    | None 
443  | 0         | None  | None        | None         | 0           | 0             | 7          | 2724         | Week1          | None          | None               | None        | 0.0    | 0.0        | rmaloney  | None 
777  | 0         | None  | None        | None         | 0           | 0             | 15         | 2509         | Week1          | None          | None               | None        | 0.0    | 0.0        | jal180    | None 
1681 | 0         | None  | None        | None         | 0           | 0             | 10         | 1332         | UnusedProblems | None          | None               | None        | 0.0    | 0.0        | pg_render | None 
267  | 0         | None  | None        | None         | 0           | 0             | 5          | 2073         | Week1          | None          | None               | None        | 0.0    | 0.0        | jbkong    | None 
```
--------------------------------------------------
### 17. CSE103_Fall2015_realtime_past_answer
***Description***:

description

***Schema***:
```
  | Field         | Type          | Null | Key | Default           | Extra                      
--|---------------|---------------|------|-----|-------------------|----------------------------
0 | id            | int(11)       | NO   | PRI | None              | auto_increment             
1 | set_id        | varchar(100)  | NO   |     | None              |                            
2 | problem_id    | varchar(100)  | NO   |     | None              |                            
3 | pg_id         | varchar(100)  | NO   |     | None              |                            
4 | user_id       | varchar(100)  | NO   |     | None              |                            
5 | source_file   | text          | YES  |     | None              |                            
6 | correct       | tinyint(1)    | YES  |     | None              |                            
7 | answer_string | varchar(1024) | YES  |     | None              |                            
8 | timestamp     | timestamp     | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP
```
***Example***:
```
This table is empty!
```
--------------------------------------------------
### 18. CSE103_Fall2015_set
***Description***:

description

***Schema***:
```
   | Field                     | Type                                                  | Null | Key | Default | Extra
---|---------------------------|-------------------------------------------------------|------|-----|---------|------
0  | set_id                    | tinyblob                                              | NO   | PRI | None    |      
1  | set_header                | text                                                  | YES  |     | None    |      
2  | hardcopy_header           | text                                                  | YES  |     | None    |      
3  | open_date                 | bigint(20)                                            | YES  |     | None    |      
4  | due_date                  | bigint(20)                                            | YES  |     | None    |      
5  | answer_date               | bigint(20)                                            | YES  |     | None    |      
6  | visible                   | int(11)                                               | YES  |     | None    |      
7  | enable_reduced_scoring    | int(11)                                               | YES  |     | None    |      
8  | assignment_type           | text                                                  | YES  |     | None    |      
9  | attempts_per_version      | int(11)                                               | YES  |     | None    |      
10 | time_interval             | int(11)                                               | YES  |     | None    |      
11 | versions_per_interval     | int(11)                                               | YES  |     | None    |      
12 | version_time_limit        | int(11)                                               | YES  |     | None    |      
13 | version_creation_time     | bigint(20)                                            | YES  |     | None    |      
14 | problem_randorder         | int(11)                                               | YES  |     | None    |      
15 | version_last_attempt_time | bigint(20)                                            | YES  |     | None    |      
16 | problems_per_page         | int(11)                                               | YES  |     | None    |      
17 | hide_score                | enum('N','Y','BeforeAnswerDate')                      | YES  |     | None    |      
18 | hide_score_by_problem     | enum('N','Y')                                         | YES  |     | None    |      
19 | hide_work                 | enum('N','Y','BeforeAnswerDate')                      | YES  |     | None    |      
20 | time_limit_cap            | enum('0','1')                                         | YES  |     | None    |      
21 | restrict_ip               | enum('No','RestrictTo','DenyFrom')                    | YES  |     | No      |      
22 | relax_restrict_ip         | enum('No','AfterAnswerDate','AfterVersionAnswerDate') | YES  |     | No      |      
23 | restricted_login_proctor  | enum('No','Yes')                                      | YES  |     | None    |      
24 | description               | text                                                  | YES  |     | None    |      
25 | hide_hint                 | int(11)                                               | YES  |     | None    |      
26 | restricted_release        | text                                                  | YES  |     | None    |      
27 | restricted_status         | float                                                 | YES  |     | None    |      
28 | reduced_scoring_date      | bigint(20)                                            | YES  |     | None    |      
```
***Example***:
```
   | answer_date | assignment_type | attempts_per_version | description | due_date   | enable_reduced_scoring | hardcopy_header | hide_hint | hide_score | hide_score_by_problem | hide_work | open_date  | problem_randorder | problems_per_page | reduced_scoring_date | relax_restrict_ip | restrict_ip | restricted_login_proctor | restricted_release | restricted_status | set_header    | set_id         | time_interval | time_limit_cap | version_creation_time | version_last_attempt_time | version_time_limit | versions_per_interval | visible
---|-------------|-----------------|----------------------|-------------|------------|------------------------|-----------------|-----------|------------|-----------------------|-----------|------------|-------------------|-------------------|----------------------|-------------------|-------------|--------------------------|--------------------|-------------------|---------------|----------------|---------------|----------------|-----------------------|---------------------------|--------------------|-----------------------|--------
15 | 1419912000  | None            | None                 | None        | 1419912000 | 1                      | defaultHeader   | None      | N          | None                  | N         | 1419112380 | None              | nan               | None                 | No                | No          | None                     | None               | None              | defaultHeader | UnusedProblems | None          | 0              | None                  | None                      | None               | nan                   | 1      
4  | 1449190800  | None            | None                 | None        | 1449190800 | 1                      | defaultHeader   | None      | N          | None                  | N         | 1448586000 | None              | nan               | None                 | No                | No          | None                     | None               | None              | defaultHeader | Week10         | None          | 0              | None                  | None                      | None               | nan                   | 1      
14 | 1446771600  | None            | None                 | None        | 1446771600 | 0                      | defaultHeader   | None      | N          | None                  | N         | 1446166800 | None              | nan               | None                 | No                | No          | None                     | None               | None              | defaultHeader | Week6          | None          | 0              | None                  | None                      | None               | nan                   | 1      
2  | 1448586000  | default         | None                 | None        | 1448586000 | 0                      | defaultHeader   | None      | None       | None                  | None      | 1447981200 | None              | 0.0               | None                 | No                | No          | None                     | None               | None              | defaultHeader | Week9          | None          | None           | None                  | None                      | None               | 0.0                   | 1      
14 | 1446771600  | None            | None                 | None        | 1446771600 | 0                      | defaultHeader   | None      | N          | None                  | N         | 1446166800 | None              | nan               | None                 | No                | No          | None                     | None               | None              | defaultHeader | Week6          | None          | 0              | None                  | None                      | None               | nan                   | 1      
```
--------------------------------------------------
### 19. CSE103_Fall2015_set_locations
***Description***:

description

***Schema***:
```
  | Field       | Type     | Null | Key | Default | Extra
--|-------------|----------|------|-----|---------|------
0 | set_id      | tinyblob | NO   | PRI | None    |      
1 | location_id | tinyblob | NO   | PRI | None    |      
```
***Example***:
```
This table is empty!
```
--------------------------------------------------
### 20. CSE103_Fall2015_set_locations_user
***Description***:

description

***Schema***:
```
  | Field       | Type     | Null | Key | Default | Extra
--|-------------|----------|------|-----|---------|------
0 | user_id     | tinyblob | NO   | PRI | None    |      
1 | set_id      | tinyblob | NO   | PRI | None    |      
2 | location_id | tinyblob | NO   | PRI | None    |      
```
***Example***:
```
This table is empty!
```
--------------------------------------------------
### 21. CSE103_Fall2015_set_user
***Description***:

description

***Schema***:
```
   | Field                     | Type                                                  | Null | Key | Default | Extra         
---|---------------------------|-------------------------------------------------------|------|-----|---------|---------------
0  | user_id                   | tinyblob                                              | NO   | MUL | None    |               
1  | set_id                    | tinyblob                                              | NO   | MUL | None    |               
2  | psvn                      | int(11)                                               | NO   | PRI | None    | auto_increment
3  | set_header                | text                                                  | YES  |     | None    |               
4  | hardcopy_header           | text                                                  | YES  |     | None    |               
5  | open_date                 | bigint(20)                                            | YES  |     | None    |               
6  | due_date                  | bigint(20)                                            | YES  |     | None    |               
7  | answer_date               | bigint(20)                                            | YES  |     | None    |               
8  | visible                   | int(11)                                               | YES  |     | None    |               
9  | enable_reduced_scoring    | int(11)                                               | YES  |     | None    |               
10 | assignment_type           | text                                                  | YES  |     | None    |               
11 | attempts_per_version      | int(11)                                               | YES  |     | None    |               
12 | time_interval             | int(11)                                               | YES  |     | None    |               
13 | versions_per_interval     | int(11)                                               | YES  |     | None    |               
14 | version_time_limit        | int(11)                                               | YES  |     | None    |               
15 | version_creation_time     | bigint(20)                                            | YES  |     | None    |               
16 | problem_randorder         | int(11)                                               | YES  |     | None    |               
17 | version_last_attempt_time | bigint(20)                                            | YES  |     | None    |               
18 | problems_per_page         | int(11)                                               | YES  |     | None    |               
19 | hide_score                | enum('N','Y','BeforeAnswerDate')                      | YES  |     | None    |               
20 | hide_score_by_problem     | enum('N','Y')                                         | YES  |     | None    |               
21 | hide_work                 | enum('N','Y','BeforeAnswerDate')                      | YES  |     | None    |               
22 | time_limit_cap            | enum('0','1')                                         | YES  |     | None    |               
23 | restrict_ip               | enum('No','RestrictTo','DenyFrom')                    | YES  |     | None    |               
24 | relax_restrict_ip         | enum('No','AfterAnswerDate','AfterVersionAnswerDate') | YES  |     | None    |               
25 | restricted_login_proctor  | enum('No','Yes')                                      | YES  |     | None    |               
26 | description               | text                                                  | YES  |     | None    |               
27 | hide_hint                 | int(11)                                               | YES  |     | None    |               
28 | restricted_release        | text                                                  | YES  |     | None    |               
29 | reduced_scoring_date      | bigint(20)                                            | YES  |     | None    |               
30 | restricted_status         | float                                                 | YES  |     | None    |               
```
***Example***:
```
     | answer_date | assignment_type | attempts_per_version | description | due_date | enable_reduced_scoring | hardcopy_header | hide_hint | hide_score | hide_score_by_problem | hide_work | open_date | problem_randorder | problems_per_page | psvn  | reduced_scoring_date | relax_restrict_ip | restrict_ip | restricted_login_proctor | restricted_release | restricted_status | set_header | set_id | time_interval | time_limit_cap | user_id  | version_creation_time | version_last_attempt_time | version_time_limit | versions_per_interval | visible
-----|-------------|-----------------|----------------------|-------------|----------|------------------------|-----------------|-----------|------------|-----------------------|-----------|-----------|-------------------|-------------------|-------|----------------------|-------------------|-------------|--------------------------|--------------------|-------------------|------------|--------|---------------|----------------|----------|-----------------------|---------------------------|--------------------|-----------------------|--------
1273 | None        | None            | None                 | None        | None     | None                   | None            | None      | None       | None                  | None      | None      | None              | None              | 29770 | None                 | None              | None        | None                     | None               | None              | None       | Week10 | None          | None           | tak068   | None                  | None                      | None               | None                  | None   
851  | None        | None            | None                 | None        | None     | None                   | None            | None      | None       | None                  | None      | None      | None              | None              | 29876 | None                 | None              | None        | None                     | None               | None              | None       | Week10 | None          | None           | vinaraya | None                  | None                      | None               | None                  | None   
1664 | None        | None            | None                 | None        | None     | None                   | None            | None      | None       | None                  | None      | None      | None              | None              | 27570 | None                 | None              | None        | None                     | None               | None              | None       | Week3  | None          | None           | ralhadda | None                  | None                      | None               | None                  | None   
1056 | None        | None            | None                 | None        | None     | None                   | None            | None      | None       | None                  | None      | None      | None              | None              | 28793 | None                 | None              | None        | None                     | None               | None              | None       | Week7  | None          | None           | hkhodada | None                  | None                      | None               | None                  | None   
1844 | None        | None            | None                 | None        | None     | None                   | None            | None      | None       | None                  | None      | None      | None              | None              | 27516 | None                 | None              | None        | None                     | None               | None              | None       | Week3  | None          | None           | kgrozav  | None                  | None                      | None               | None                  | None   
```
--------------------------------------------------
### 22. CSE103_Fall2015_setting
***Description***:

description

***Schema***:
```
  | Field | Type         | Null | Key | Default | Extra
--|-------|--------------|------|-----|---------|------
0 | name  | varchar(255) | NO   | PRI | None    |      
1 | value | text         | YES  |     | None    |      
```
***Example***:
```
  | name       | value    
--|------------|----------
0 | db_version | 3.1415926
```
--------------------------------------------------
### 23. CSE103_Fall2015_user
***Description***:

description

***Schema***:
```
   | Field          | Type     | Null | Key | Default | Extra
---|----------------|----------|------|-----|---------|------
0  | user_id        | tinyblob | NO   | PRI | None    |      
1  | first_name     | text     | YES  |     | None    |      
2  | last_name      | text     | YES  |     | None    |      
3  | email_address  | text     | YES  |     | None    |      
4  | student_id     | text     | YES  |     | None    |      
5  | status         | text     | YES  |     | None    |      
6  | section        | text     | YES  |     | None    |      
7  | recitation     | text     | YES  |     | None    |      
8  | comment        | text     | YES  |     | None    |      
9  | useMathView    | int(11)  | YES  |     | None    |      
10 | displayMode    | text     | YES  |     | None    |      
11 | showOldAnswers | int(11)  | YES  |     | None    |      
```
***Example***:
```
    | comment | displayMode | email_address     | first_name   | last_name | recitation | section | showOldAnswers | status | student_id | useMathView | user_id 
----|---------|-------------|-------------------|--------------|-----------|------------|---------|----------------|--------|------------|-------------|---------
5   | None    | MathJax     | aalhaida@ucsd.edu | Amal         | Alhaidari | None       | 849807  | 1.0            | C      | A98069538  | None        | aalhaida
246 | None    | None        | edcole@ucsd.edu   | Erin Dorothy | Cole      | None       | 849807  | nan            | C      | A11858829  | None        | edcole  
201 | None    | None        | ajabasa@ucsd.edu  | Andrew Mazon | Jabasa    | None       | 849807  | nan            | C      | A11479202  | None        | ajabasa 
172 | None    | MathJax     | tol003@ucsd.edu   | Tong         | Lee       | None       | 849807  | 1.0            | C      | A12380292  | None        | tol003  
61  | None    | MathJax     | lywong@ucsd.edu   | Lok Yi       | Wong      | None       | 849807  | 1.0            | C      | A10659556  | None        | lywong  
```
--------------------------------------------------
### 24. CSE103_Fall2015_user_variables
***Description***:

description

***Schema***:
```
  | Field      | Type          | Null | Key | Default | Extra
--|------------|---------------|------|-----|---------|------
0 | set_id     | varchar(255)  | NO   | MUL | None    |      
1 | problem_id | int(11)       | NO   | MUL | None    |      
2 | user_id    | varchar(255)  | NO   | MUL | None    |      
3 | name       | varchar(255)  | NO   | MUL | None    |      
4 | value      | float         | NO   |     | None    |      
5 | string     | varchar(1024) | NO   |     | None    |      
```
***Example***:
```
     | name | problem_id | set_id | string          | user_id  | value
-----|------|------------|--------|-----------------|----------|------
1776 | $Ac  | 1          | Week2  | {1,2,3,4,5,6}   | lmfink   | 0.0  
658  | $max | 1          | Week2  | 15              | kdb006   | 15.0 
1429 | $rs  | 1          | Week2  | {6,7,8,9,10,11} | cagatep  | 0.0  
717  | $min | 1          | Week2  | 4               | rbdoming | 4.0  
1252 | $max | 1          | Week2  | 13              | krkelkar | 13.0 
```
--------------------------------------------------
