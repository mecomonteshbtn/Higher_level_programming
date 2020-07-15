# 0x0E. SQL - More queries 

## Resources:books:
Read or watch:
* [How To Create a New User and Grant Permissions in MySQL](https://intranet.hbtn.io/rltoken/u4h2MXcCQfadszlRMQy-gw)
* [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://intranet.hbtn.io/rltoken/9JjDTdvflUSxwxLNfW8sPg)
* [MySQL constraints](https://intranet.hbtn.io/rltoken/u1P3WmgxehiqwcLBMlksUA)
* [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/YYpPtkqFeKSCsAU4Y_y3Og)
* [Basic query operation: the join](https://intranet.hbtn.io/rltoken/npLCp3WasK0SUSUQqCF25A)
* [SQL technique: multiple joins and the distinct keyword](https://intranet.hbtn.io/rltoken/GmRLMhkY-pPvjcpzyDvmRg)
* [SQL technique: join types](https://intranet.hbtn.io/rltoken/ryjyRRN7696rJV0maP03Xw)
* [SQL technique: union and minus](https://intranet.hbtn.io/rltoken/L7Fi5w8GZG5MSdQZ19e88g)
* [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/V9vpLbtkFwV4EZYoiz2NBA)
* [The Seven Types of SQL Joins](https://intranet.hbtn.io/rltoken/ySKSdhFeMDddea07XrDzeQ)
* [MySQL Tutorial](https://intranet.hbtn.io/rltoken/-uqP0a89xUl3SsmV_ZtxRA)
* [SQL Style Guide](https://intranet.hbtn.io/rltoken/jn4SHgwVtOJF0LQYPEIs-g)
* [MySQL 5.7 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/YjNAE7DcadDbT_a7iI0sYw)

---
## Learning Objectives:bulb:
What you should learn from this project:

* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION
---
<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F331296116314414522%2F&psig=AOvVaw0NQ3ZOsWA5BaB9oluBROke&ust=1594833409992000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJDWj8mfzeoCFQAAAAAdAAAAABAD">
---
## General Requirements

*    Allowed editors: vi, vim, emacs
*    All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
*    All your files should end with a new line
*    All your SQL queries should have a comment just before (i.e. syntax above)
*    All your files should start by a comment describing the task
*    All SQL keywords should be in uppercase (SELECT, WHERE…)
*    A README.md file, at the root of the folder of the project, is mandatory
*    The length of your files will be tested using wc

More Info
Comments for your SQL file:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

Install MySQL 5.7 on Ubuntu 14.04 LTS

$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$
```
Don’t forget your root password

If you had before MySQL 5.5 installed, please run these 2 commands after the installation of the version 5.7:
```
$ mysql_upgrade -u root -p
Password: 
$ sudo service mysql restart
```
If you have some issues to upgrade to 5.7, don’t hesitate to cleanup your server of any MySQL packages: sudo apt-get remove --purge mysql-server mysql-client mysql-common
Use “container-on-demand” to run MySQL

*    Ask for container Ubuntu 14.04 - Python 3.4
*    Connect via SSH
*    Or via the WebTerminal
*    In the container, you should start MySQL before playing with it:
```
$ service mysql start
 * MySQL Community Server 5.7.8-rc is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$

In the container, credentials are root/root
How to import a SQL dump

$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
---

### [0. My privileges!](./0-privileges.sql)
* Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
```
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_1' on host 'localhost'
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
guillaume@ubuntu:~/$ 
```

### [1. Root user](./1-create_user.sql)
* Write a script that creates the MySQL server user user_0d_1. 
*    user_0d_1 should have all privileges on your MySQL server
*    The user_0d_1 password should be set to user_0d_1_pwd
*    If the user user_0d_1 already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
guillaume@ubuntu:~/$ 
```

### [2. Read user](./2-create_read_user.sql)
* Write a script that creates the database hbtn_0d_2 and the user user_0d_2. 
*    user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
*    The user_0d_2 password should be set to user_0d_2_pwd
*    If the database hbtn_0d_2 already exists, your script should not fail
*    If the user user_0d_2 already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
Grants for user_0d_2@localhost
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost'
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost'
guillaume@ubuntu:~/$ 
```

### [3. Always a name](./3-force_name.sql)
* Write a script that creates the table force_name on your MySQL server.
*    force_name description:
*        id INT
*        name VARCHAR(256) can’t be null
*    The database name will be passed as an argument of the mysql command
*    If the table force_name already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id, name) VALUES (89, "Holberton School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Holberton School
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id) VALUES (333);' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1364 (HY000) at line 1: Field 'name' doesn't have a default value
guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Holberton School
guillaume@ubuntu:~/$ 
```

### [4. ID can't be null](./4-never_empty.sql)
* Write a script that creates the table id_not_null on your MySQL server.
*    id_not_null description:
*        id INT with the default value 1
*        name VARCHAR(256)
*    The database name will be passed as an argument of the mysql command
*    If the table id_not_null already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Holberton School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Holberton School
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (name) VALUES ("Holberton");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Holberton School
1   Holberton
guillaume@ubuntu:~/$ 
```

### [5. Unique ID](./5-unique_id.sql)
* Write a script that creates the table unique_id on your MySQL server.
*    unique_id description:
*        id INT with the default value 1 and must be unique
*        name VARCHAR(256)
*    The database name will be passed as an argument of the mysql command
*    If the table unique_id already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Holberton School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Holberton School
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Holberton");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry '89' for key 'id'
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id  name
89  Holberton School
guillaume@ubuntu:~/$ 
```

### [6. States table](./6-states.sql)
* Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
*    states description:
*        id INT unique, auto generated, can’t be null and is a primary key
*        name VARCHAR(256) can’t be null
*    If the database hbtn_0d_usa already exists, your script should not fail
*    If the table states already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 6-states.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
guillaume@ubuntu:~/$ 
```

### [7. Cities table](./7-cities.sql)
* Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
*    cities description:
*        id INT unique, auto generated, can’t be null and is a primary key
*        state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
*        name VARCHAR(256) can’t be null
*    If the database hbtn_0d_usa already exists, your script should not fail
*    If the table cities already exists, your script should not fail
```
guillaume@ubuntu:~/$ cat 7-cities.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (10, "Paris");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
ERROR 1452 (23000) at line 1: Cannot add or update a child row: a foreign key constraint fails (`hbtn_0d_usa`.`cities`, CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`))
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
guillaume@ubuntu:~/$ 
```

### [8. Cities of California](./8-cities_of_california_subquery.sql)
* Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
*    The states table contains only one record where name = California (but the id can be different, as per the example)
*    Results must be sorted in ascending order by cities.id
*    You are not allowed to use the JOIN keyword
*    The database name will be passed as an argument of the mysql command
```
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
4   Utah
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
guillaume@ubuntu:~/$ cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   San Francisco
2   San Jose
guillaume@ubuntu:~/$ 
```

### [9. Cities by States](./9-cities_by_state_join.sql)
* Write a script that lists all cities contained in the database hbtn_0d_usa.
*    Each record should display: cities.id - cities.name - states.name
*    Results must be sorted in ascending order by cities.id
*    You can use only one SELECT statement
*    The database name will be passed as an argument of the mysql command
```
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
4   Utah
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
guillaume@ubuntu:~/$ cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name    name
1   San Francisco   California
2   San Jose    California
4   Page    Arizona
6   Paris   Texas
7   Houston Texas
8   Dallas  Texas
guillaume@ubuntu:~/$ 
```

### [10. Genre ID by show](./10-genre_id_by_show.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download

How to import a SQL dump
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
*    Each record should display: tv_shows.title - tv_show_genres.genre_id
*    Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
*    You can use only one SELECT statement
*    The database name will be passed as an argument of the mysql command
```
guillaume@ubuntu:~/$ cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
guillaume@ubuntu:~/$ 
```

### [11. Genre ID for all shows](./11-genre_id_all_shows.sql)
* Import the database dump of hbtn_0d_tvshows to your MySQL server: download (same as 10-genre_id_by_show.sql)
Write a script that lists all shows contained in the database hbtn_0d_tvshows.
*    Each record should display: tv_shows.title - tv_show_genres.genre_id
*    Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
*    If a show doesn’t have a genre, display NULL
*    You can use only one SELECT statement
*    The database name will be passed as an argument of the mysql command
```
guillaume@ubuntu:~/$ cat 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Better Call Saul    NULL
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
Homeland    NULL
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
guillaume@ubuntu:~/$ 
```

### [12. No genre](./12-no_genre.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 11-genre_id_all_shows.sql)
Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
*    Each record should display: tv_shows.title - tv_show_genres.genre_id
*    Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
*    You can use only one SELECT statement
*    The database name will be passed as an argument of the mysql command
```
guillaume@ubuntu:~/$ cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Better Call Saul    NULL
Homeland    NULL
guillaume@ubuntu:~/$ 
```

### [13. Number of shows by genre](./13-count_shows_by_genre.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql)
Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
*    Each record should display: <TV Show genre> - <Number of shows linked to this genre>
*    First column must be called genre
*    Second column must be called number_of_shows
*    Don’t display a genre that doesn’t have any shows linked
*    Results must be sorted in descending order by the number of shows linked
*    You can use only one SELECT statement
*    The database name will be passed as an argument of the mysql command
```
guillaume@ubuntu:~/$ cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
genre   number_of_shows
Drama   5
Comedy  4
Mystery 2
Crime   2
Suspense    2
Thriller    2
Adventure   1
Fantasy 1
guillaume@ubuntu:~/$ 
```

### [14. My genres](./14-my_genres.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 13-count_shows_by_genre.sql)
Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
*    The tv_shows table contains only one record where title = Dexter (but the id can be different)
*    Each record should display: tv_genres.name
*    Results must be sorted in ascending order by the genre name
*    You can use only one SELECT statement
*    The database name will be passed as an argument of the mysql command
```
guillaume@ubuntu:~/$ cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
name
Crime
Drama
Mystery
Suspense
Thriller
guillaume@ubuntu:~/$ 
```

### [15. Only Comedy](./15-comedy_only.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 14-my_genres.sql)
Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
*    The tv_genres table contains only one record where name = Comedy (but the id can be different)
*    Each record should display: tv_shows.title
*    Results must be sorted in ascending order by the show title
*    You can use only one SELECT statement
*    The database name will be passed as an argument of the mysql command
```
guillaume@ubuntu:~/$ cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title
New Girl
Silicon Valley
The Big Bang Theory
The Last Man on Earth
guillaume@ubuntu:~/$ 
```

### [16. List shows and genres](./16-shows_by_genre.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 15-comedy_only.sql)
Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
*    If a show doesn’t have a genre, display NULL in the genre column
*    Each record should display: tv_shows.title - tv_genres.name
*    Results must be sorted in ascending order by the show title and genre name
*    You can use only one SELECT statement
*    The database name will be passed as an argument of the mysql command
```
guillaume@ubuntu:~/$ cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   name
Better Call Saul    NULL
Breaking Bad    Crime
Breaking Bad    Drama
Breaking Bad    Suspense
Breaking Bad    Thriller
Dexter  Crime
Dexter  Drama
Dexter  Mystery
Dexter  Suspense
Dexter  Thriller
Game of Thrones Adventure
Game of Thrones Drama
Game of Thrones Fantasy
Homeland    NULL
House   Drama
House   Mystery
New Girl    Comedy
Silicon Valley  Comedy
The Big Bang Theory Comedy
The Last Man on Earth   Comedy
The Last Man on Earth   Drama
guillaume@ubuntu:~/$ 
```

### [17. Not my genre](./100-not_my_genres.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 16-shows_by_genre.sql)
Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
*    The tv_shows table contains only one record where title = Dexter (but the id can be different)
*    Each record should display: tv_genres.name
*    Results must be sorted in ascending order by the genre name
*    You can use a maximum of two SELECT statement
*    The database name will be passed as an argument of the mysql command
```
guillaume@ubuntu:~/$ cat 100-not_my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
name
Adventure
Comedy
Fantasy
guillaume@ubuntu:~/$ 
```

### [18. No Comedy tonight!](./101-not_a_comedy.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 100-not_my_genres.sql)
Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
*    The tv_genres table contains only one record where name = Comedy (but the id can be different)
*    Each record should display: tv_shows.title
*    Results must be sorted in ascending order by the show title
*    You can use a maximum of two SELECT statement
*    The database name will be passed as an argument of the mysql command
```
guillaume@ubuntu:~/$ cat 101-not_a_comedy.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title
Better Call Saul
Breaking Bad
Dexter
Game of Thrones
Homeland
House
guillaume@ubuntu:~/$ 
```

### [19. Rotten tomatoes](./102-rating_shows.sql)
* Import the database hbtn_0d_tvshows_rate dump to your MySQL server: download
Write a script that lists all shows from hbtn_0d_tvshows_rate by their rating.
*    Each record should display: tv_shows.title - rating sum
*    Results must be sorted in descending order by the rating
*    You can use only one SELECT statement
*    The database name will be passed as an argument of the mysql command
```
guillaume@ubuntu:~/$ cat 102-rating_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
Enter password: 
title   rating
Better Call Saul    163
Homeland    145
Silicon Valley  82
Game of Thrones 79
Dexter  24
House   21
Breaking Bad    16
The Last Man on Earth   10
The Big Bang Theory 0
New Girl    0
guillaume@ubuntu:~/$ 
```

### [20. Best genre](./103-rating_genres.sql)
* Import the database dump from hbtn_0d_tvshows_rate to your MySQL server: download (same as 102-rating_shows.sql)
Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
*    Each record should display: tv_genres.name - rating sum
*    Results must be sorted in descending order by their rating
*    You can use only one SELECT statement
*    The database name will be passed as an argument of the mysql command
```
guillaume@ubuntu:~/$ cat 103-rating_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
Enter password: 
name    rating
Drama   150
Comedy  92
Adventure   79
Fantasy 79
Mystery 45
Crime   40
Suspense    40
Thriller    40
guillaume@ubuntu:~/$ 
```

---

## Author
* **Robinson Montes** - [mecomonteshbtn](https://github.com/mecomonteshbtn)