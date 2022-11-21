--Exercise1
SELECT lang.name FROM language lang;

SELECT f.title,f.description,l.name FROM language l RIGHT OUTER JOIN film f ON l.language_id=f.language_id;
SELECT f.title,f.description,l.name FROM language l LEFT OUTER JOIN film f ON l.language_id=f.language_id;

CREATE TABLE new_film(
	id SERIAL PRIMARY KEY NOT NULL,
	name VARCHAR(60) NOT NULL
);

INSERT INTO new_film(name) VALUES('The 100'),('Grimm'),('Original');

CREATE TABLE  customer_review(
	review_id SERIAL PRIMARY KEY NOT NULL,
	film_id INTEGER NOT NULL,
	language_id INTEGER NOT NULL,
	title VARCHAR(50) NOT NULL,
	score INTEGER NOT NULL CHECK(score>=1 AND score<=10),
	review_text TEXT NOT NULL, 
	last_update DATE NOT NULL,
	FOREIGN KEY(film_id) REFERENCES new_film(id ) ON DELETE CASCADE,
	FOREIGN KEY(language_id) REFERENCES language(language_id)
);

INSERT INTO customer_review(
	film_id,language_id,title,score,review_text,last_update
) 
VALUES(
	(
		SELECT id FROM new_film WHERE name='The 100'
		),
	(
		SELECT language_id FROM language WHERE name='English'
		),
	'Durée',5,'La série ne dure pas assez par épisode ',CURRENT_DATE
	),
		(
			(
				SELECT id FROM new_film WHERE name='Grimm'
				),
			(
				SELECT language_id FROM language WHERE name='French'
				),
		'Appréciation',3,"C'est trop dingue cette série là",CURRENT_DATE
		);

DELETE FROM new_film WHERE name='The 100';


--Exercise2

UPDATE film SET language_id=(SELECT language_id FROM language WHERE name='French') WHERE film_id BETWEEN 1 AND 100;

DROP TABLE customer_review; 

SELECT COUNT(r.rental_id) FROM rental r WHERE r.return_date IS NULL;

SELECT f.title ,f.rental_rate FROM rental r INNER JOIN inventory i ON i.inventory_id=r.inventory_id INNER JOIN film f ON f.film_id=i.film_id
WHERE r.return_date IS NULL AND f.rental_rate IN(SELECT MAX(rental_rate) FROM film)  LIMIT 30;

SELECT f.title FROM film f INNER JOIN film_actor fa ON f.film_id=fa.film_id  WHERE description ILIKE '%a lutteur de sumo%' AND 
fa.actor_id=(SELECT actor_id FROM actor WHERE first_name='Penelope' AND last_name='Monroe');

SELECT f.title FROM film f INNER JOIN film_category fc ON f.film_id=fc.film_id  WHERE (f.length/60)<1 AND f.rating='R' 
AND fc.category_id=(SELECT category_id FROM category WHERE name ILIKE '%documentary%');

SELECT f.title FROM film f INNER JOIN inventory i ON f.film_id=i.film_id INNER JOIN rental r ON r.inventory_id=i.inventory_id WHERE f.rental_rate>4 AND r.return_date 
BETWEEN '2005-07-28' AND '2005-08-01' AND r.customer_id=(SELECT customer_id FROM customer WHERE first_name='Matthew' AND last_name='Mahan');

SELECT f.title FROM film f INNER JOIN inventory i ON f.film_id=i.film_id INNER JOIN rental r ON r.inventory_id=i.inventory_id WHERE ((f.title ILIKE'%boat%') OR (f.description ILIKE'%boat%')) 
AND r.return_date IS NOT NULL AND f.replacement_cost> (SELECT AVG(replacement_cost) FROM film) AND r.customer_id=(SELECT customer_id FROM customer WHERE first_name='Matthew' AND last_name='Mahan');
