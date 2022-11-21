-- Database: dvdrental
-- Exercise1
SELECT rating ,count(film_id) FROM film GROUP BY rating;

SELECT  film_id,title,description,rating FROM film WHERE rating IN ('G','PG-13') AND (film.length/60)<2 AND rental_rate<3 ORDER BY title ASC;

UPDATE customer SET first_name='CHEICK',last_name='KEITA',email='keita@gmail.com',last_update=CURRENT_DATE WHERE customer_id=1;

UPDATE address SET address='16 NELSON MANDELA' WHERE  address_id=(SELECT address_id FROM customer WHERE customer_id=1);


-- Exercise2
UPDATE students SET birth_date='02/11/1998' WHERE last_name='Benichou';

UPDATE students SET last_name='Guez' WHERE first_name='David';

DELETE FROM students WHERE last_name='Benichou' AND first_name='Lea';

SELECT COUNT(*) FROM students;

SELECT COUNT(*) FROM students WHERE birth_date > '1/01/2000';


ALTER TABLE students ADD COLUMN math_grade INTEGER ;

UPDATE students SET math_grade=80 WHERE id_students=1;
UPDATE students SET math_grade=90 WHERE id_students IN (1,4);
UPDATE students SET math_grade=40 WHERE id_students=6;
SELECT COUNT(*) FROM students WHERE math_grade>83;
INSERT INTO students VALUES(6,'Omer', 'Simpson', (SELECT birth_date FROM students WHERE last_name='Simpson' AND first_name='Omer'),70);
SELECT SUM(math_grade) as SumNote FROM students;


-- Exercise3
CREATE TABLE purchases (
 	purchases_id SERIAL PRIMARY KEY NOT NULL,
	customer_id INTEGER NOT NULL,
	items_id INTEGER NOT NULL,
	quantity_purchased INTEGER NOT NULL,
	FOREIGN KEY(customer_id) REFERENCES customers(id_customers),
	FOREIGN KEY(items_id) REFERENCES items(id_items)
);


INSERT INTO purchases(customer_id,items_id,quantity_purchased) VALUES((SELECT id_customers FROM customers WHERE last_name='Scott' AND first_name='Scott'),(SELECT id_items FROM items WHERE libelle='fan' ),1);
INSERT INTO purchases(customer_id,items_id,quantity_purchased) VALUES((SELECT id_customers FROM customers WHERE last_name='Johnson' AND first_name='Melanie'),(SELECT id_items FROM items WHERE libelle='large desk' ),10);
INSERT INTO purchases(customer_id,items_id,quantity_purchased) VALUES((SELECT id_customers FROM customers WHERE last_name='Jones' AND first_name='Greg'),(SELECT id_items FROM items WHERE libelle='small desk' ),2);

SELECT * FROM purchases;
SELECT * FROM purchases pu INNER JOIN customers cu ON pu.customer_id=cu.id_customers;
SELECT * FROM purchases WHERE customer_id=5;
SELECT * FROM purchases pu INNER JOIN items i ON pu.items_id=i.id_items  WHERE i.libelle IN ('large desk','small desk');


SELECT cu.first_name,cu.last_name, i.libelle FROM customers cu INNER JOIN purchases pu ON cu.id_customers=pu.customer_id  INNER JOIN items i ON pu.items_id=i.id_items;

INSERT INTO purchases(customer_id,quantity_purchased) VALUES((SELECT id_customers FROM customers WHERE last_name='Jones' AND first_name='Sandra'),2);
-- Ne marche pas parce que item_id est fixé comme not null