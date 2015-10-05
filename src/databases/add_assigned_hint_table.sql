DELETE FROM {{course_name}}_assigned_hint;
ALTER TABLE {{course_name}}_assigned_hint
CHANGE assigned assigned_time timestamp;
ALTER TABLE {{course_name}}_assigned_hint
ADD assigned varchar(1);