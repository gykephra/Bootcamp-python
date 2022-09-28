-- Database: bootcampp

-- DROP DATABASE IF EXISTS bootcampp;

-- CREATE DATABASE bootcampp
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'French_France.1252'
--     LC_CTYPE = 'French_France.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

CREATE TABLE students(
 id_students SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (50) NOT NULL,
 birth_date DATE NOT NULL
)

INSERT INTO students(first_name, last_name, birth_date) ABORT
VALUES('Marc', 'Benichou','02/11/1998'), ('Yoan', 'Cohen', '03/12/2010'), ('Lea', 'Benichou','27/07/1987')