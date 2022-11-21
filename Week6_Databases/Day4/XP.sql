
SELECT first_name as Firstname, last_name as Lastname FROM employees;
SELECT DISTINCT(department_id) FROM employees;
SELECT * FROM employees ORDER BY first_name DESC;
SELECT first_name as PRENOM, last_name as NOM, salary as SALAIRE, (salary*0.15) as PF FROM employees;
SELECT employee_id, first_name as PRENOM, last_name as NOM, salary as SALAIRE FROM employees ORDER BY salary ASC;
SELECT SUM(salary) as SALAIRE_TOTAL FROM employees;
SELECT MAX(salary) AS SALAIRE_MAXIMAL, MIN(salary) as SALAIRE_MINIMAL FROM employees;
SELECT AVG(salary) as SALAIRE_MOYEN FROM employees;
SELECT COUNT(employee_id) AS NOMBRE_TRAVAILLEUR FROM employees;
SELECT UPPER(first_name) FROM employees;
SELECT SUBSTRING(first_name for 3) FROM employees;
SELECT CONCAT(first_name, ' ', last_name) as IDENTITE FROM employees;
SELECT first_name, last_name, CHAR_LENGTH(first_name)+CHAR_LENGTH(last_name) as LONGUEUR_NOM_COMPLET FROM employees;
SELECT first_name FROM employees WHERE first_name ~ '^[0-9]$';
SELECT * FROM employees LIMIT 10;

--Restriction Et Tri
SELECT first_name, last_name, salary FROM employees WHERE salary BETWEEN 10000 and 15000;
SELECT first_name, last_name, hire_date FROM employees WHERE hire_date BETWEEN '1987-01-01' and '1987-12-31';
SELECT * FROM employees WHERE first_name LIKE '%c%' AND first_name LIKE '%e%';
 SELECT employees.last_name, jobs.job_title, employees.salary 
 FROM employees JOIN jobs ON jobs.job_id = employees.job_id 
 WHERE jobs.job_id NOT IN (SELECT DISTINCT jobs.job_id
      FROM jobs
      WHERE jobs.job_title = 'Programmer'
    ) AND employees.salary NOT IN (4500, 10000, 15000);

SELECT last_name FROM employees WHERE CHAR_LENGTH(last_name) = 6;
SELECT last_name FROM employees WHERE SUBSTRING(last_name FROM 3 for 1) LIKE '%e%';
SELECT DISTINCT(jobs.job_title) FROM jobs JOIN employees ON jobs.job_id = employees.job_id;
SELECT * FROM employees WHERE last_name IN ('JONES', 'BLAKE', 'SCOTT', 'KING', 'FORD')