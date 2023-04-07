USE dojos_and_ninjas_schema;
-- Query: Create 3 new dojos
INSERT INTO dojos (name) VALUES ("Bellevue"), ("Princeton"), ("Talahasee");

SELECT * FROM dojos;
-- Query: Delete the 3 dojos you just created
DELETE FROM dojos WHERE id > 0;

-- Query: Create 3 more dojos
INSERT INTO dojos (name) VALUES ("Lao Tzu's"), ("Bobs Burgers"), ("Mickys Joint");

-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (`first_name`, `last_name`, age, `dojo_id`)
VALUES ("Linda", "Hicks", 34, 4),
        ("Mandy", "Hislop", 45, 4),
        ("Scooby", "Doo", 7, 4);

-- Query: Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas (`first_name`, `last_name`, age, `dojo_id`)
VALUES ("Dicky", "Fines", 85, 5),
        ("Donald", "Duck", 25, 5),
        ("Jack", "London", 32, 5);

-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO ninjas (`first_name`, `last_name`, age, `dojo_id`)
VALUES ("Shloop", "Sales", 60, 6),
        ("Dippy", "Dan", 18, 6),
        ("Don", "Juan", 14, 6);

-- Query: Retrieve all the ninjas from the first dojo
SELECT * from ninjas 
WHERE dojo_id = 4;

-- Query: Retrieve all the ninjas from the last dojo
SELECT * from ninjas 
WHERE dojo_id = 6;

-- Query: Retrieve the last ninja's dojo
Select * from dojos 
WHERE id = 6;


