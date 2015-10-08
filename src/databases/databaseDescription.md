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
  | answer_id | answer_string | id | part_id | problem_id | score | set_id            | timestamp           | user_id 
--|-----------|---------------|----|---------|------------|-------|-------------------|---------------------|---------
0 | 875       | F             | 1  | 1       | 1          | 1     | Intro.readingTest | 2013-09-28 22:56:36 | holi    
1 | 875       | F             | 2  | 2       | 1          | 1     | Intro.readingTest | 2013-09-28 22:56:36 | holi    
2 | 875       | T             | 3  | 3       | 1          | 1     | Intro.readingTest | 2013-09-28 22:56:36 | holi    
3 | 875       | T             | 4  | 4       | 1          | 1     | Intro.readingTest | 2013-09-28 22:56:36 | holi    
4 | 953       | F             | 5  | 1       | 1          | 1     | Intro.readingTest | 2013-09-28 23:39:34 | jacontre
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
  | answer        | part_id | problem_id | set_id | user_id 
--|---------------|---------|------------|--------|---------
0 | {1,2,3,4,5,6} | 1       | 1          | Week2  | grecinto
1 | {5,7,9,11}    | 2       | 1          | Week2  | grecinto
2 | {1,2,3,4,5,6} | 1       | 1          | Week2  | rsamuail
3 | {3,5,7,9}     | 2       | 1          | Week2  | rsamuail
4 | {1,2,3,4,5,6} | 1       | 1          | Week2  | l5han   
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
--|--------------------|------------|----------------------------------------------------|----------------------|-------------------|---------
0 | 15                 | None       |    ƒ   completeProblems                      | None                 | None              | yfreund 
1 | 665                | None       |       completeSets
133   completeProblems | None                 | None              | dleroy  
2 | 1045               | None       |    ’   completeSets
209   completeProblems | None                 | None              | halou   
3 | 940                | None       |    ˜   completeSets
188   completeProblems | None                 | None              | jagustin
4 | 340                | None       |    †   completeSetsÄ   completeProblems    | None                 | None              | r1luong 
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
--|----------------------------------|------------|---------
0 | FymoYXr0nuqGtcKtzZ2QI8hNem6v9syU | 1443996953 | yfreund 
1 | eNPdqxvLPvz1HH2jXDbWwMGockVGrrae | 1444266528 | rsmurlo 
2 | 4Grl9TpcjUnd09bC9H3E3hwRGs9Ezl9G | 1443907776 | dpereira
3 | Cgujw6ruJfPLucXa64aKXKXjBDRDEj3T | 1443741191 | aysee   
4 | 32LBT3QgyWxu7wFtPy63wGZUz2VKupK3 | 1386616595 | dhyee   
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
--|------------------------------------------------------------------------------------------------------------|--------
0 | $6$.yjkiJBBHNgLc9Z5$v1KkA6W7Ty7sPHGqK87GnAEjzG5N84NVy40bIsyR0Zzi6AGgZq4d4.MDEmukvgiC/u1A8Sd.GaDDiyQMRe15p0 | sayao  
1 | LTtaaDBCqZ7Nc                                                                                              | yfreund
2 | $6$EZj4.ds2DzBZQv.R$/mJAcw5vfrJQtTdECBEvwfoWVSU3KG0EB88kNZSNuQB6Tdd9Dn5tazloDFSDmLN5dBRfmsNi4f.wC3oXtBe5o1 | muy002 
3 | 2.9r9vM8BjCl2                                                                                              | mabid  
4 | J0axR3nY/P.xg                                                                                              | babney 
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
  | answer_id | answer_string | comment_string | course_id   | problem_id | scores | set_id                | source_file                                  | timestamp  | user_id
--|-----------|---------------|----------------|-------------|------------|--------|-----------------------|----------------------------------------------|------------|--------
0 | 1         | 123	          | None           | UCSD_CSE103 | 2          | 0      | TestPreparationCB     | setTestPreparation/events8_hint.pg           | 1371175363 | wentao 
1 | 2         | 2	3	4	        | None           | UCSD_CSE103 | 4          | 000    | TestPreparationCB     | setTestPreparation/cond6_hint.pg             | 1371175400 | wentao 
2 | 3         | 2	3	          | None           | UCSD_CSE103 | 4          | 11     | Statistics_appetizers | local/setStatistics_appetizers/ThreeCards.pg | 1379190808 | yfreund
3 | 4         | None          | None           | UCSD_CSE103 | 1          | None   | Orientation           | setOrientation/prob01.pg                     | 1380312884 | dleroy 
4 | 5         | None          | None           | UCSD_CSE103 | 2          | None   | Orientation           | setOrientation/prob02.pg                     | 1380313058 | dleroy 
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
--|------------|---------
0 | 0          | flhernan
1 | 0          | atorr   
2 | 0          | krkelkar
3 | 10         | yfreund 
4 | 0          | z3meng  
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
  | flags | max_attempts | problem_id | set_id        | showMeAnother | showMeAnotherCount | source_file                            | value
--|-------|--------------|------------|---------------|---------------|--------------------|----------------------------------------|------
0 | None  | -1           | 6          | Week1         | None          | None               | Reorganized/Orientation/prob06.pg      | 1    
1 | None  | -1           | 5          | Week1         | None          | None               | Reorganized/Orientation/prob05.pg      | 1    
2 | None  | -1           | 4          | Week1         | None          | None               | Reorganized/Orientation/prob04.pg      | 1    
3 | None  | -1           | 3          | Week1         | None          | None               | Reorganized/Orientation/prob03.pg      | 1    
4 | None  | -1           | 6          | BasicExamples | None          | None               | local/setBasicExamples/event_tree_6.pg | 1    
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
  | attempted | flags | last_answer | max_attempts | num_correct | num_incorrect | problem_id | problem_seed | set_id | showMeAnother | showMeAnotherCount | source_file | status | sub_status | user_id  | value
--|-----------|-------|-------------|--------------|-------------|---------------|------------|--------------|--------|---------------|--------------------|-------------|--------|------------|----------|------
0 | 0         | None  | None        | None         | 0           | 0             | 14         | 1839         | Week1  | None          | None               | None        | 0.0    | 0.0        | bbarmeye | None 
1 | 0         | None  | None        | None         | 0           | 0             | 1          | 118          | Week1  | None          | None               | None        | 0.0    | 0.0        | bbatenga | None 
2 | 0         | None  | None        | None         | 0           | 0             | 13         | 3935         | Week1  | None          | None               | None        | 0.0    | 0.0        | bbarmeye | None 
3 | 0         | None  | None        | None         | 0           | 0             | 5          | 2737         | Week1  | None          | None               | None        | 0.0    | 0.0        | bbarmeye | None 
4 | 0         | None  | None        | None         | 0           | 0             | 7          | 3517         | Week1  | None          | None               | None        | 0.0    | 0.0        | dabaraja | None 
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
  | answer_date | assignment_type | attempts_per_version | description | due_date   | enable_reduced_scoring | hardcopy_header | hide_hint | hide_score | hide_score_by_problem | hide_work | open_date  | problem_randorder | problems_per_page | reduced_scoring_date | relax_restrict_ip | restrict_ip | restricted_login_proctor | restricted_release | restricted_status | set_header    | set_id        | time_interval | time_limit_cap | version_creation_time | version_last_attempt_time | version_time_limit | versions_per_interval | visible
--|-------------|-----------------|----------------------|-------------|------------|------------------------|-----------------|-----------|------------|-----------------------|-----------|------------|-------------------|-------------------|----------------------|-------------------|-------------|--------------------------|--------------------|-------------------|---------------|---------------|---------------|----------------|-----------------------|---------------------------|--------------------|-----------------------|--------
0 | 1409781840  | default         | None                 | None        | 1409781840 | 0                      | defaultHeader   | None      | None       | None                  | None      | 1409177040 | None              | 0.0               | None                 | No                | No          | None                     | None               | None              | defaultHeader | BasicExamples | None          | None           | None                  | None                      | None               | 0.0                   | 1      
1 | 1443744000  | default         | None                 | None        | 1443744000 | 1                      | defaultHeader   | None      | None       | None                  | None      | 1443139200 | None              | 0.0               | None                 | No                | No          | None                     | None               | None              | defaultHeader | Week1         | None          | None           | None                  | None                      | None               | 0.0                   | 1      
2 | 1448586000  | default         | None                 | None        | 1448586000 | 0                      | defaultHeader   | None      | None       | None                  | None      | 1447981200 | None              | 0.0               | None                 | No                | No          | None                     | None               | None              | defaultHeader | Week9         | None          | None           | None                  | None                      | None               | 0.0                   | 1      
3 | 1418241600  | None            | None                 | None        | 1418241600 | 1                      | defaultHeader   | None      | N          | None                  | N         | 1417636800 | None              | nan               | None                 | No                | No          | None                     | None               | None              | defaultHeader | FinalPractice | None          | 0              | None                  | None                      | None               | nan                   | 1      
4 | 1449190800  | None            | None                 | None        | 1449190800 | 1                      | defaultHeader   | None      | N          | None                  | N         | 1448586000 | None              | nan               | None                 | No                | No          | None                     | None               | None              | defaultHeader | Week10        | None          | 0              | None                  | None                      | None               | nan                   | 1      
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
--|-------------|-----------------|----------------------|-------------|----------|------------------------|-----------------|-----------|------------|-----------------------|-----------|-----------|-------------------|-------------------|-------|----------------------|-------------------|-------------|--------------------------|--------------------|-------------------|------------|--------|---------------|----------------|----------|-----------------------|---------------------------|--------------------|-----------------------|--------
0 | None        | None            | None                 | None        | None     | None                   | None            | None      | None       | None                  | None      | None      | None              | None              | 8390  | None                 | None              | None        | None                     | None               | None              | None       | Week1  | None          | None           | ybowen   | None                  | None                      | None               | None                  | None   
1 | None        | None            | None                 | None        | None     | None                   | None            | None      | None       | None                  | None      | None      | None              | None              | 29896 | None                 | None              | None        | None                     | None               | None              | None       | Week10 | None          | None           | yeh013   | None                  | None                      | None               | None                  | None   
2 | None        | None            | None                 | None        | None     | None                   | None            | None      | None       | None                  | None      | None      | None              | None              | 8388  | None                 | None              | None        | None                     | None               | None              | None       | Week1  | None          | None           | bbatra   | None                  | None                      | None               | None                  | None   
3 | None        | None            | None                 | None        | None     | None                   | None            | None      | None       | None                  | None      | None      | None              | None              | 8387  | None                 | None              | None        | None                     | None               | None              | None       | Week1  | None          | None           | bbatenga | None                  | None                      | None               | None                  | None   
4 | None        | None            | None                 | None        | None     | None                   | None            | None      | None       | None                  | None      | None      | None              | None              | 8386  | None                 | None              | None        | None                     | None               | None              | None       | Week1  | None          | None           | bbarmeye | None                  | None                      | None               | None                  | None   
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
  | comment | displayMode | email_address    | first_name   | last_name | recitation | section | showOldAnswers | status | student_id | useMathView | user_id
--|---------|-------------|------------------|--------------|-----------|------------|---------|----------------|--------|------------|-------------|--------
0 | None    | MathJax     | c4du@ucsd.edu    | Chongyang    | Du        | None       | 849807  | 1.0            | C      | A91117207  | None        | c4du   
1 | None    | None        | kew060@ucsd.edu  | Kevin        | Wong      | None       | 849807  | nan            | C      | A12319704  | None        | kew060 
2 | None    | None        | kmphan@ucsd.edu  | Khoi Minh    | Phan      | None       | 849807  | nan            | C      | A12291728  | None        | kmphan 
3 | None    | None        | yfreund@ucsd.edu | Yoav         | Freund    | None       | None    | nan            | C      | yfreund    | None        | yfreund
4 | None    | None        | krau@ucsd.edu    | Kristopher B | Rau       | None       | 849807  | nan            | C      | A11965837  | None        | krau   
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
  | name | problem_id | set_id | string                 | user_id  | value
--|------|------------|--------|------------------------|----------|------
0 | $Ac  | 1          | Week2  | {1,2,3,4,5,6}          | grecinto | 0.0  
1 | $rs  | 1          | Week2  | {4,5,6,7,8,9,10,11,12} | grecinto | 0.0  
2 | $A   | 1          | Week2  | {5,7,9,11}             | grecinto | 0.0  
3 | $min | 1          | Week2  | 4                      | grecinto | 4.0  
4 | $max | 1          | Week2  | 12                     | grecinto | 12.0 
```
--------------------------------------------------
