ALTER TABLE {{course_name}}_user
ADD hint int(11);
UPDATE {{course_name}}_user
SET hint = FLOOR(0 + (RAND()*2));
