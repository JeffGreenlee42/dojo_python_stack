USE books_schema;

-- Query: Create 5 different users: Jane Amsden, Emily Dixon, Theodore Dostoevsky, William Shapiro, Lao Xiu--
INSERT INTO users (first_name, last_name)
VALUES ("Jane", "Amsden"),
("Emily", "Dixon"),
("Theodore", "Dostoevsky"),
("William", "Shapiro"),
("Lao", "Xiu");

-- Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
INSERT INTO books (title, `num_of_pages`)
VALUES ("C Sharp", 579),
("Java", 892),
("Python", 679),
("PHP", 479),
("Ruby", 520);

-- Query: Change the name of the C Sharp book to C#
UPDATE books 
SET title = "C#"
WHERE title = "C Sharp";

-- Query: Change the first name of the 4th user to Bill
UPDATE users
SET first_name = "Bill"
WHERE users.id = 4;

-- Query: Have the first user favorite the first 2 books
INSERT INTO favorites (`user_id`, `book_id`)
VALUES (1, 1), (1, 2);

-- Query: Have the second user favorite the first 3 books
INSERT INTO favorites (`user_id`, `book_id`)
VALUES (2, 1), (2, 2), (2, 3);

-- Query: Have the third user favorite the first 4 books
INSERT INTO favorites (`user_id`, `book_id`)
VALUES (3, 1), (3, 2), (3, 3), (3, 4);

-- Query: Have the fourth user favorite all the books
INSERT INTO favorites (`user_id`, `book_id`)
VALUES (4, 1), (4, 2), (4, 3), (4, 4), (4, 5);


