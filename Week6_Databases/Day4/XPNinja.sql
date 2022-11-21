CREATE DATABASE "hr. backup"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

SELECT first_name, last_name,salary FROM employees WHERE salary >(SELECT salary FROM employees WHERE last_name='Bull');
select * from employees where country_id='US'
SELECT e.first_name, e.last_name FROM employees e 
WHERE e.manager_id IN(SELECT DISTINCT em.employee_id FROM employees em
				  WHERE em.department_id IN (SELECT DISTINCT d.department_id FROM departments d
									   WHERE d.location_id IN(SELECT l.location_id FROM locations l
														  WHERE l.country_id =(SELECT co.country_id FROM countries co
																		WHERE co.country_name='United States of America'))));

SELECT first_name, last_name FROM employees WHERE (employee_id IN (SELECT manager_id FROM employees));

SELECT first_name, last_name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);

SELECT first_name, last_name, salary FROM employees  WHERE employees.salary = (SELECT min_salary FROM jobs WHERE employees.job_id = jobs.job_id);

SELECT b.first_name,b.last_name FROM employees b WHERE NOT EXISTS (SELECT 'X' FROM employees a WHERE a.manager_id = b.employee_id);

SELECT employee_id, first_name FROM employees AS A WHERE salary > (SELECT AVG(salary) FROM employees WHERE department_id = A.department_id);

SELECT DISTINCT salary FROM employees e1 WHERE 5 = (SELECT COUNT(DISTINCT salary) FROM employees  e2 WHERE e1.salary <= e2.salary);
SELECT DISTINCT salary FROM employees e1 WHERE 4 = (SELECT COUNT(DISTINCT salary) FROM employees  e2 WHERE e2.salary <= e1.salary);
SELECT * FROM departments WHERE department_id NOT IN (select department_id FROM employees);



SELECT location_id, street_address, city, state_province, country_name FROM locations NATURAL JOIN countries;

SELECT first_name, last_name, department_id, department_name FROM employees JOIN departments USING (department_id);

SELECT e.first_name, e.last_name, e.job_id, e.department_id, d.department_name FROM employees e JOIN departments d ON (e.department_id = d.department_id) 
JOIN locations l ON (d.location_id = l.location_id) WHERE LOWER(l.city) = 'London';

SELECT W1.employee_id as "Emp_id" , W1.last_name AS "Employee", W2.employee_id AS "Manager ID", W2.last_name AS "Manager" FROM employees W1 JOIN employees W2
ON W1.manager_id= W2.employee_id;

SELECT department_name AS 'Department Name', COUNT(*) AS 'No of Employees' FROM departments INNER JOIN employees ON employees.department_id = departments.department_id 
GROUP BY departments.department_id, department_name ORDER BY department_name;

SELECT employee_id, job_title, end_date-start_date Days FROM job_history NATURAL JOIN jobs WHERE department_id=90;

SELECT d.department_name, e.first_name, l.city FROM departments d JOIN employees e ON (d.manager_id = e.employee_id) JOIN locations l USING (location_id);

SELECT job_title, AVG(salary) FROM employees NATURAL JOIN jobs GROUP BY job_title;

SELECT department_name, first_name, last_name,hire_date, salary,date_part('year',age(now(),hire_date)) Experience FROM departments w1 JOIN employees w2 
ON (w1.manager_id = w2.employee_id) WHERE date_part('year',age(now(),hire_date))>15;


UPDATE employees SET phone_number = REPLACE(phone_number, '124', '999') WHERE phone_number LIKE '%124%';

SELECT left(first_name, 8),REPEAT('$', FLOOR(salary/1000)) 'SALARY($)', salary FROM employees ORDER BY salary DESC;

SELECT UPPER(CONCAT(SUBSTRING(first_name,1,1),last_name,SUBSTRING(email,POSITION('@'IN email)))) FROM employees;

SELECT employee_id, REVERSE(SUBSTR(REVERSE(email), 4)) AS Email_ID FROM employees;

SELECT job_title, SUBSTR(job_title,1, INSTR(job_title, ' ')-1) FROM jobs;

SELECT first_name "Name",LENGTH(first_name) "Length" FROM employees WHERE first_name LIKE 'J%' OR first_name LIKE 'M%' OR first_name LIKE 'A%'ORDER BY first_name ;

SELECT first_name, LPAD(salary, 10, '$') SALARY FROM employees;