SELECT first_name,last_name,id_customers FROM (SELECT first_name,last_name,id_customers FROM customers ORDER BY id_customers DESC LIMIT 2 ) tmp ORDER BY id_customers ASC ; 
DELETE FROM purchases pu WHERE pu.customer_id= (SELECT id_customers FROM customers WHERE last_name='Scott'); 
SELECT * FROM customers WHERE last_name='Scott'; 
SELECT * FROM customers cu LEFT OUTER JOIN purchases pu ON pu.customer_id=cu.id_customers; 
SELECT * FROM customers cu RIGHT OUTER JOIN purchases pu ON pu.customer_id=cu.id_customers;
