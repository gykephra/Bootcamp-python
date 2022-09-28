-- Database: public

-- DROP DATABASE IF EXISTS public;

-- CREATE DATABASE public
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'French_France.1252'
--     LC_CTYPE = 'French_France.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False; 
CREATE TABLE items(
 items_id SERIAL PRIMARY KEY,
 items_list VARCHAR (50) NOT NULL,
 items_price INT NOT NULL 
)

CREATE TABLE custumers(
 custumers_id SERIAL PRIMARY KEY,
 fist_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (50) NOT NULL
 )
 
 INSERT INTO items(items_list, items_price) 
 VALUES('Small_desk', 100), ('Large_desk', 300), ('Fan', 80);
 
 INSERT INTO custumers(first_name, last_name) 
 VALUES('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson');
 
 SELECT * FROM items;
 SELECT * FROM items WHERE 
 
 