         
         CREATE TABLE dogs (
            name TEXT,
            breed TEXT,
            age INTEGER
         );

         sqlite> .tables
         dogs
         sqlite> .read basic.sql
            ...> SELECT * FROM dogs;
         INSERT INTO dogs (name, breed, age) VALUES ("Blue", "Scottish Fold", 3);
         SELECT name, age FROM dogs;
         SELECT * FROM dogs WHERE breed IS NOT "Chihuahua";
         SELECT * FROM dogs WHERE breed IS NOT "Chihuahua" AND breed IS NOT "Lab";
         SELECT * FROM dogs WHERE age > 5;
         SELECT * FROM dogs WHERE name LIKE "%gg%";
         SELECT * FROM dogs
