-- SELECT * FROM customer
-- SELECT first_name ||' '|| last_name AS full_name FROM customer
-- SELECT DISTINCT create_date  FROM customer
-- SELECT * FROM customer ORDER BY first_name ASC
-- SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC   
-- SELECT address, phone from address WHERE district = 'Texas'
-- SELECT * FROM film WHERE film_id =  ---- INCOMPLETE
-- SELECT film_id, title, description, rental_duration, rental_rate FROM film  WHERE title ILIKE 'AC%'
-- SELECT film_id, title, rental_rate FROM film ORDER BY rental_rate ASC FETCH FIRST 10 ROWS ONLY
-- SELECT film_id, title, rental_rate FROM film ORDER BY rental_rate ASC FETCH FIRST 10 ROWS ONLY OFFSET 10
-- SELECT * FROM customer NATURAL JOIN payment ORDER BY customer_id 
-- SELECT customer.customer_id, customer.first_name, customer.last_name, amount, payment_date FROM customer NATURAL JOIN payment ORDER BY customer_id
-- SELECT film_id, title FROM film WHERE film_id NOT IN (SELECT film_id FROM inventory)
-- SELECT country.country_id, country, city, city.city_id FROM country NATURAL JOIN city


