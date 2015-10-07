### 1. CSE103_Fall2015_achievement
***Description***:

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
--------------------------------------------------
### 2. CSE103_Fall2015_achievement_user
***Description***:

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
--------------------------------------------------
### 3. CSE103_Fall2015_answers_by_part
***Description***:

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
--------------------------------------------------
### 4. CSE103_Fall2015_assigned_hint
***Description***:

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
--------------------------------------------------
### 5. CSE103_Fall2015_assigned_hint_feedback
***Description***:

***Schema***:
```
  | Field            | Type         | Null | Key | Default           | Extra                      
--|------------------|--------------|------|-----|-------------------|----------------------------
0 | assigned_hint_id | int(11)      | NO   | MUL | None              |                            
1 | feedback         | varchar(255) | NO   |     | None              |                            
2 | timestamp        | timestamp    | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP
```
--------------------------------------------------
### 6. CSE103_Fall2015_assigned_hint_filter
***Description***:

***Schema***:
```
  | Field          | Type      | Null | Key | Default           | Extra                      
--|----------------|-----------|------|-----|-------------------|----------------------------
0 | hint_id        | int(11)   | NO   | PRI | None              |                            
1 | hint_filter_id | int(11)   | NO   | PRI | None              |                            
2 | assigned       | timestamp | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP
3 | trigger_cond   | text      | YES  |     | None              |                            
```
--------------------------------------------------
### 7. CSE103_Fall2015_correct_answers
***Description***:

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
--------------------------------------------------
### 8. CSE103_Fall2015_global_user_achievement
***Description***:

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
--------------------------------------------------
### 9. CSE103_Fall2015_hint
***Description***:

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
--------------------------------------------------
### 10. CSE103_Fall2015_hint_filter
***Description***:

***Schema***:
```
  | Field       | Type         | Null | Key | Default | Extra         
--|-------------|--------------|------|-----|---------|---------------
0 | id          | int(11)      | NO   | PRI | None    | auto_increment
1 | filter_name | varchar(255) | NO   |     | None    |               
```
--------------------------------------------------
### 11. CSE103_Fall2015_key
***Description***:

***Schema***:
```
  | Field             | Type       | Null | Key | Default | Extra
--|-------------------|------------|------|-----|---------|------
0 | user_id           | tinyblob   | NO   | PRI | None    |      
1 | key_not_a_keyword | text       | YES  |     | None    |      
2 | timestamp         | bigint(20) | YES  |     | None    |      
```
--------------------------------------------------
### 12. CSE103_Fall2015_password
***Description***:

***Schema***:
```
  | Field    | Type     | Null | Key | Default | Extra
--|----------|----------|------|-----|---------|------
0 | user_id  | tinyblob | NO   | PRI | None    |      
1 | password | text     | YES  |     | None    |      
```
--------------------------------------------------
### 13. CSE103_Fall2015_past_answer
***Description***:

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
--------------------------------------------------
### 14. CSE103_Fall2015_permission
***Description***:

***Schema***:
```
  | Field      | Type     | Null | Key | Default | Extra
--|------------|----------|------|-----|---------|------
0 | user_id    | tinyblob | NO   | PRI | None    |      
1 | permission | int(11)  | YES  |     | None    |      
```
--------------------------------------------------
### 15. CSE103_Fall2015_problem
***Description***:

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
--------------------------------------------------
### 16. CSE103_Fall2015_problem_user
***Description***:

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
--------------------------------------------------
### 17. CSE103_Fall2015_realtime_past_answer
***Description***:

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
--------------------------------------------------
### 18. CSE103_Fall2015_set
***Description***:

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
--------------------------------------------------
### 19. CSE103_Fall2015_set_locations
***Description***:

***Schema***:
```
  | Field       | Type     | Null | Key | Default | Extra
--|-------------|----------|------|-----|---------|------
0 | set_id      | tinyblob | NO   | PRI | None    |      
1 | location_id | tinyblob | NO   | PRI | None    |      
```
--------------------------------------------------
### 20. CSE103_Fall2015_set_locations_user
***Description***:

***Schema***:
```
  | Field       | Type     | Null | Key | Default | Extra
--|-------------|----------|------|-----|---------|------
0 | user_id     | tinyblob | NO   | PRI | None    |      
1 | set_id      | tinyblob | NO   | PRI | None    |      
2 | location_id | tinyblob | NO   | PRI | None    |      
```
--------------------------------------------------
### 21. CSE103_Fall2015_set_user
***Description***:

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
--------------------------------------------------
### 22. CSE103_Fall2015_setting
***Description***:

***Schema***:
```
  | Field | Type         | Null | Key | Default | Extra
--|-------|--------------|------|-----|---------|------
0 | name  | varchar(255) | NO   | PRI | None    |      
1 | value | text         | YES  |     | None    |      
```
--------------------------------------------------
### 23. CSE103_Fall2015_user
***Description***:

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
--------------------------------------------------
### 24. CSE103_Fall2015_user_variables
***Description***:

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
--------------------------------------------------
