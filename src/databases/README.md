#Files#

* `create_hint_databases.sh`: Create hint database tables for new homework set. 
##### 
```
bash create_hint_databases.sh <set_name>
```
* `save_answers.py`: Create/Update two database tables: <course>_correct_answers and <course>_user_variables.
#####  
```
export PYTHONPATH="$PYTHONPATH:/opt/Webwork_AdaptiveHints/src/servers"
python save_answers.py -c <course_name> -s <set_id>
```
* `past_answer_to_answers_by_part.py`: Create table <course>_answers_by_part. Running constantly to split up the answers per question into answers per part. This is controlled by an upstart init file `past-answer-daemon.conf` The logs go to `/var/log/upstart/past-answer-daemon.log`. To restart the daemon do the following
##### 
```
cd /etc/init/
sudo initctl start past-answer_daemon
```
* `describe_tables.py`: reads tables from webwork database and creates the markdown description at `databaseDescription.md`.



#Database#

The full description of the database available in [databaseDescription.md](https://github.com/cse103/Webwork_AdaptiveHints/blob/master/src/databases/databaseDescription.md).
