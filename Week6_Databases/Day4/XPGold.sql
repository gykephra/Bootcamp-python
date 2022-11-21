CREATE DATABASE "hr. backup"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
	
UPDATE employees SET email='not available',commission_pct=0.10 WHERE department_id=110;
UPDATE employees SET email='available' WHERE department_id=(SELECT department_id FROM departments WHERE department_name='Accounting');
UPDATE employees SET salary=8000 WHERE employee_id=105 AND salary< 5000;


SELECT COUNT(DISTINCT job_id) FROM employees;
SELECT COUNT(employee_id), job_id FROM employees GROUP BY job_id;
SELECT (MAX(salary)- MIN(salary)) AS difference FROM employees;
SELECT e.manager_id, e.salary FROM employees e WHERE e.salary=(SELECT MIN(salary) FROM employees WHERE manager_id=e.manager_id);
SELECT AVG(e.salary) AS Average, j.job_title FROM employees e,jobs j WHERE e.job_id=j.job_id AND j.job_title !='Programmer' GROUP BY j.job_title ;
SELECT AVG(e.salary) AS Average, d.department_name FROM employees e,departments d  WHERE e.department_id=d.department_id 
GROUP BY d.department_name HAVING COUNT(employee_id)>10;


ALTER TABLE locations RENAME COLUMN state_province TO state;
ALTER TABLE locations ADD PRIMARY KEY(location_id);


CREATE TABLE new_countries(
	country_id SERIAL PRIMARY KEY,
	country_name VARCHAR(20) CHECK(country_name IN ('India','Italy','China'))
);

CREATE TABLE copy_new_countries AS SELECT * FROM new_countries;

CREATE TABLE new_jobs (
	job_id SERIAL PRIMARY KEY,
	job_title VARCHAR(50) DEFAULT '', 
	min_salary INTEGER DEFAULT 8000, 
	max_salary INTEGER CHECK(max_salary<25000) DEFAULT NULL 
);

CREATE TABLE new_employees (
	employee_id INTEGER PRIMARY KEY,
	first_name VARCHAR(50) , 
	last_name VARCHAR(50) , 
	email  VARCHAR(50) , 
	phone_number  VARCHAR(50) ,
	hire_date DATE, 
	job_id INTEGER NOT NULL,
	salary INTEGER NOT NULL,
	FOREIGN KEY(job_id) REFERENCES new_jobs(job_id)
);

CREATE TABLE new_job_history (
	employee_id INTEGER ,
	start_date DATE , 
	end_date DATE, 
	job_id INTEGER NOT NULL,
	FOREIGN KEY(job_id) REFERENCES new_jobs(job_id) ON DELETE SET NULL ON UPDATE SET NULL,
	FOREIGN KEY(employee_id) REFERENCES new_employees(employee_id)
);

INSERT INTO new_countries (country_name) VALUES ('India');

INSERT INTO new_countries (country_name) VALUES ('India'),('Italy'),('China');

INSERT INTO copy_new_countries (country_name) VALUES ('India'),('Italy'),('China');

NSERT INTO new_jobs (job_title, min_salary, max_salary) VALUES ('Programmer',20000,22000);

INSERT INTO new_employees (employee_id, first_name, last_name, email, phone_number ,hire_date, job_id,salary) 
VALUES (1,'Ali','Oued','ouedal@gmail.com','53658488','2022-11-12',(SELECT job_id FROM new_jobs WHERE job_title='ingeneer'),55000);
