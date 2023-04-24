USE sakila;


SELECT * FROM customer;
SELECT * from city;

-- SELECT * What query would you run to get all the customers inside city_id = 312?
-- Your query should return customer first name, last name, email, and address.

SELECT CONCAT(customer.first_name, " ", customer.last_name) AS Name, customer.email AS "Email",
CONCAT(address.address, " ", address.address2, " ", city.city, " ", address.postal_code) AS "Address"
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE city.city_id = 312;

-- What query would you run to get all comedy films?
-- Your query should return film title, description, release year, rating, special features, and genre (category).

SELECT film.title AS "Title", film.description "Description", film.release_year AS "Release Year",
film.rating AS "Rating", film.special_features AS "Special Features", category.name AS "Genre"
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = "Comedy";

-- What query would you run to get all the films joined by actor_id=5?
-- Your query should return the actor id, actor name, film title, description, and release year.

SELECT actor.actor_id AS "Actor ID", CONCAT(actor.first_name, " ", actor.last_name) AS "Name",
film.title AS "Film", film.description AS "Description", film.release_year AS "Release Year"
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;

-- What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)?
-- Your query should return customer first name, last name, email, and address.


SELECT CONCAT(customer.first_name, " ", customer.last_name) AS "Customer Name", customer.email AS "Email",
CONCAT(address.address, " ", address.address2, " ", city.city, " ", address.postal_code) AS "Address"
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE address.city_id IN (1, 42, 312, 459);

-- What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", 
-- joined by actor_id = 15? Your query should return the film title, description, release year, rating, and special feature. 
-- Hint: You may use LIKE function in getting the 'behind the scenes' part.

SELECT film.title AS "Title", film.description AS "Description", film.release_year AS "Year", 
film.rating AS "Rating", film.special_features AS "Special Feature"
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
WHERE film.special_features LIKE "behind the scenes" AND film.rating = "G" AND film_actor.actor_id = 15;

-- What query would you run to get all the actors that joined in the film_id = 369? 
-- Your query should return the film_id, title, actor_id, and actor_name.

SELECT film.film_id AS "Film ID", film.title AS "Title", actor.actor_id AS "Actor ID", 
CONCAT(actor.first_name, " ", actor.last_name) AS "Actor Name"
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;


-- What query would you run to get all drama films with a rental rate of 2.99?
-- Your query should return film title, description, release year, rating, special features, and genre (category).

SELECT film.title AS "Title", film.description AS "Description", film.release_year AS "Year",
film.rating AS "Rating", film.special_features AS "Special Features", category.name as "Genre"
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = "Drama" AND film.rental_rate = 2.99;

-- What query would you run to get all the action films which are joined by SANDRA KILMER?
-- Your query should return film title, description, release year, rating, special features, genre (category),
-- and actor's first name and last name.

SELECT film.title AS "Title", film.description AS "Description", film.release_year AS "Year",
film.rating AS "Rating", film.special_features AS "Special Features", category.name as "Genre",
CONCAT(actor.first_name, " ", actor.last_name) AS "Actor Name"
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
JOIN film_actor ON film.film_id = film_actor.film_id 
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE category.name = "Action" AND actor.first_name = "Sandra" AND actor.last_name = "Kilmer" ;
