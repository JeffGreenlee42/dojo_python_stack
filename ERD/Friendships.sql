USE Friendships;

SELECT * from users;
SELECT * FROM friendships;

-- Query: Have user 1 be friends with user 2, 4 and 6
INSERT INTO Friendships.users (`first_name`, `last_name`)
VALUES ("Amy", "Giver"), 
("Eli", "Byers"),
("Big", "Bird"),
("Kermit", "The Frog"),
("Marky", "Mark"),å
("Humphrey", "Bogart");

-- Query: Have user 1 be friends with user 2, 4 and 6
INSERT INTO Friendships.friendships (`user_id`, `friend_id`)
VALUES (1, 2), (1, 4), (1, 6);

-- Query: Have user 2 be friends with user 1, 3 and 5
INSERT INTO Friendships.friendships (`user_id`, `friend_id`)
VALUES (2, 1), (2, 3), (2, 5);

-- Query: Have user 3 be friends with user 2 and 5
INSERT INTO Friendships.friendships (`user_id`, `friend_id`)
VALUES (3, 2), (3, 5);

-- Query: Have user 4 be friends with user 3
INSERT INTO Friendships.friendships (`user_id`, `friend_id`)
VALUES (4, 3);

-- Query: Have user 5 be friends with user 1 and 6
INSERT INTO Friendships.friendships (`user_id`, `friend_id`)
VALUES (5, 1), (5, 6);

-- Query: Have user 6 be friends with user 2 and 3
INSERT INTO Friendships.friendships (`user_id`, `friend_id`)
VALUES (6, 2), (6, 3);

-- Query: Display the relationships created as shown in the table in the above image
SELECT users.first_name AS "First Name", users.last_name AS "Last Name", user2.first_name AS "Friend's First Name", user2.last_name "Friends Last Name" 
FROM users
JOIN friendships ON users.id = friendships.friend_id
LEFT JOIN users AS user2 ON user2 .id = friendships.user_id
ORDER BY users.first_name;

-- NINJA Query: Return all users who are friends with the first user, make sure their names are displayed in results.
SELECT user2.first_name AS "Friend's First Name", user2.last_name "Friends Last Name"
FROM users
JOIN friendships ON users.id = friendships.friend_id
LEFT JOIN users AS user2 ON user2 .id = friendships.user_id
WHERE users.id = 1
ORDER BY user2.first_name;


-- NINJA Query: Return the count of all friendships
SELECT concat(users.first_name, " ",  users.last_name)  AS "Name", COUNT(friendships.user_id) AS "Number of Friends"
FROM users
JOIN friendships ON users.id = friendships.friend_id
LEFT JOIN users AS user2 ON user2.id = friendships.user_id
GROUP BY users.id
ORDER BY users.first_name;

-- NINJA Query: Find out who has the most friends and return the count of their friends.
SELECT concat(users.first_name, " ",  users.last_name)  AS "Name", COUNT(*) totalFriends
FROM users
JOIN friendships ON users.id = friendships.friend_id
LEFT JOIN users AS user2 ON user2.id = friendships.user_id
GROUP BY Name
ORDER BY totalFriends DESC
LIMIT 1;


-- NINJA Query: Return the friends of the third user in alphabetical order
SELECT CONCAT(user2.first_name, " ", user2.last_name) 
FROM users
JOIN friendships ON users.id = friendships.friend_id
LEFT JOIN users AS user2 ON user2 .id = friendships.user_id
WHERE users.id = 3
ORDER BY user2.first_name;

SELECT * FROM friendships