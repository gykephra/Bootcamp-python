-- Exercise1
SELECT * FROM rental WHERE return_date IS NULL;
SELECT * FROM customer cu INNER JOIN rental r ON r.customer_id=cu.customer_id WHERE r.return_date IS NULL;
WHERE fc.category_id=(SELECT category_id FROM category WHERE name='Action') 
AND fa.actor_id=(SELECT actor_id FROM actor WHERE last_name='Swank' AND first_name='Joe');

-- Exercise2
SELECT COUNT(s.store_id) as Nombre, ci.city,co.country FROM store s INNER JOIN address ad ON s.address_id=ad.address_id INNER JOIN city ci ON
ci.city_id=ad.city_id INNER JOIN country co ON co.country_id=ci.country_id GROUP BY ci.city,co.country ;

SELECT SUM(f.length), i.store_id FROM film f INNER JOIN inventory i ON f.film_id=i.film_id GROUP BY i.store_id;

SELECT cu.first_name,cu.last_name ,ci.city FROM customer cu INNER JOIN address ad ON cu.address_id=ad.address_id INNER JOIN city ci ON ci.city_id=ad.city_id
INNER JOIN store s ON cu.store_id=s.store_id WHERE cu.address_id=s.address_id;
