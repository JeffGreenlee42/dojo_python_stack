-- Query: Create 3 new users
INSERT INTO users (`first_name`, `last_name`, email)
VALUES ("Jeff", "Greenlee", "banjo1@gmail.com"),
        ("Bob", "Godhead", "bob.godhead@angles.com"),
        ("Shirly", "Jackson", "Shirly.jackson@compuserve.com");

-- Query: Retrieve all the users
SELECT * FROM users;

-- Query: Retrieve the first user using their email address
SELECT * FROM users WHERE email = "banjo1@gmail.com";

-- Query: Retrieve the last user using their id
SELECT * FROM users WHERE id = 3;

-- Query: Change the user with id=3 so their last name is Pancakes
UPDATE users SET last_name = "Pancakes"
WHERE id = 3;

-- Query: Delete the user with id=2 from the database
DELETE users FROM WHERE id = 2;

-- Query: Get all the users, sorted by their first name
SELECT * from users ORDER BY first_name;

-- BONUS Query: Get all the users, sorted by their first name in descending order
SELECT * from users ORDER BY first_name DESC;
