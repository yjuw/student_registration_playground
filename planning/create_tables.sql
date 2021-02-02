--DROP TABLE MEMBER CASCADE;

CREATE TABLE IF NOT EXISTS Course(
course_id SERIAL PRIMARY KEY,
course_name TEXT,
course_name_short TEXT,
course_capacity INTEGER,
course_currently_enrolled INTEGER,
course_instructor TEXT,
course_section_number INTEGER
course_location TEXT
);

CREATE TABLE IF NOT EXISTS Member(
net_id TEXT PRIMARY KEY,
first_name TEXT,
middle_name TEXT,
last_name TEXT,
hashed_pass TEXT,
role TEXT
);

CREATE TABLE IF NOT EXISTS Enrolled_Class(
Enrolled_Class_id SERIAL PRIMARY KEY,
Enrolled_Class_Member_id TEXT REFERENCES Member(net_id),
Enrolled_Course_id INTEGER REFERENCES Course(course_id)
);