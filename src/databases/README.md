#Files#

* `create_hint_databases.sh`: Take in class name. Will create hint database tables for new class set. Needs to be run when creating a new homework set.
* `save_answers.py`: Run with `python save_answers.py -c <course_name> -s <set_id>`. Create/Update two database tables, `correct_answers` and `user_variables`. Needs to be run when a new set is created or new problems are added to problem set.
* `past_answer_to_answers_by_part.py`: Create table 'answers_by_part' for `CSE103_Fall2015`. Needs to be running constantly to basically split up the answers per question into answers per part. This is controlled by an upstart init file at `/etc/init/past-answer-daemon.conf` on server. To restart the past-answer-daemon.conf, run `sudo initctl start past-answer-daemon`. It will replace start with stop/restart in the file. The logs go to `/var/log/upstart/past-answer-daemon.log`
* `describe_tables.py`: reads tables from webwork database and creates the markdown description at `databaseDescription.md`.
* `create_hint_databases.sh` is the script which creates hint related tables in the webwork database. It executes SQL scripts `hint_tables_template.sql`, `hint_filter_template.sql`, `realtime_answers_template.sql` and `test_hint_tables_template.sql` via python script `render_hint_tables.py` which does the job.



#Database#

The full description of the database available in [databaseDescription.md](https://github.com/cse103/Webwork_AdaptiveHints/blob/master/src/databases/databaseDescription.md).
