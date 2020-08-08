# 0x0F. Python - Object-relational mapping

---
## Background Context

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
With an ORM:
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something. 

---
## Resources:books:
Read or watch:
* [Object-relational mappers](https://intranet.hbtn.io/rltoken/IqdjUaZ31ZfP6eT-lTyUkA)
* [mysqlclient/MySQLdb documentation](https://intranet.hbtn.io/rltoken/rMJpVJ1_YjMWfvY00I7Kpw)
* [MySQLdb tutorial](https://intranet.hbtn.io/rltoken/KskI6xMlQCYJyE0UVPJfKQ)
* [SQLAlchemy tutorial](https://intranet.hbtn.io/rltoken/9JWveMwNKe3IUErdEbDsUQ)
* [SQLAlchemy](https://intranet.hbtn.io/rltoken/E9dLS6Shaezq4ivnGxN_RA)
* [mysqlclient/MySQLdb](https://intranet.hbtn.io/rltoken/SSoBE3ckyGFi3NexCH3nuw)
* [Introduction to SQLAlchemy](https://intranet.hbtn.io/rltoken/I5bvhPGTOu3_-T-4jpN-hg)
* [Flask SQLAlchemy](https://intranet.hbtn.io/rltoken/UvaHESHeqlRA0Z0uQFi0_A)
* [10 common stumbling blocks for SQLAlchemy newbies](https://intranet.hbtn.io/rltoken/Zb8Yc2WycLLYX8gnLlwZKw)
* [Python SQLAlchemy Cheatsheet](https://intranet.hbtn.io/rltoken/XHPAX7-ydSou2BLWHII8Vw)
* [SQLAlchemy ORM Tutorial for Python Developers](https://intranet.hbtn.io/rltoken/aeLSQ039BhLhamU2BjqsOw)

---
## Learning Objectives:bulb:
What you should learn from this project:

* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script 
* What ORM means
* How to map a Python Class to a MySQL table

---
## General Requirements

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* Your files will be executed with MySQLdb version 1.3.x
* Your files will be executed with SQLAlchemy version 1.2.x
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* You are not allowed to use execute with sqlalchemy

---
## More Info
Install MySQLdb module version 1.3.x
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__ 
'1.3.10'
```
Install SQLAlchemy module version 1.2.x
```
$ pip3 install SQLAlchemy==1.2.5
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.2.5'
```
Also, you can have this warming message:
```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
```
You can ignore it.

---
### [0. Get all states](./0-select_states.py)
* Write a script that lists all states from the database hbtn_0e_0_usa: 

* Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by states.id
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed

### [1. Filter states](./1-filter_states.py)
* Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa: 

* Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by states.id
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed

### [2. Filter states by user input](./2-my_filter_states.py)
* Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

* Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* You must use format to create the SQL query with the user input
* Results must be sorted in ascending order by states.id
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed

### [3. SQL Injection...](./3-my_safe_filter_states.py)
* Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/0x0F$ 

What? Empty?

Yes, it’s an SQL injection to delete all records of a table…

Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from [MySQL injections!](https://en.wikipedia.org/wiki/SQL_injection)

* Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by states.id
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed

### [4. Cities by states](./4-cities_by_state.py)
* Write a script that lists all cities from the database hbtn_0e_4_usa 

* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by cities.id
* You can use only execute() once
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed

### [5. All cities by state](./5-filter_cities.py)
* Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa 

* Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
* You must use the module MySQLdb (import MySQLdb)
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by cities.id
* You can use only execute() once
* The results must be displayed as they are in the example below
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas

guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii

guillaume@ubuntu:~/0x0F$  
```
No test cases needed

### [6. First state model](./model_state.py)
* Write a python file that contains the class definition of a State and an instance Base = declarative_base():

* State class:
    * inherits from Base Tips
    * links to the MySQL table states
    * class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
    * class attribute name that represents a column of a string with maximum 128 characters and can’t be null
* You must use the module SQLAlchemy
* Your script should connect to a MySQL server running on localhost at port 3306
* WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)
```
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql
-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;
SHOW CREATE TABLE states;

guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
guillaume@ubuntu:~/0x0F$ cat 6-model_state.py
#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

guillaume@ubuntu:~/0x0F$ ./6-model_state.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed


### [7. All states via SQLAlchemy](./7-model_state_fetch_all.py)
* Write a script that lists all State objects from the database hbtn_0e_6_usa 

* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by states.id
* The results must be displayed as they are in the example below
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql
-- Insert states
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password: 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed

### [8. First state](./8-model_state_fetch_first.py)
* Write a script that prints the first State object from the database hbtn_0e_6_usa 

* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* The state you display must be the first in states.id
* You are not allowed to fetch all states from the database before displaying the result
* The results must be displayed as they are in the example below
* If the table states is empty, print Nothing followed by a new line
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed

### [9. Contains `a`](./9-model_state_filter_a.py)
* Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa 

* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by states.id
* The results must be displayed as they are in the example below
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed

### [10. Get a state](./10-model_state_my_get.py)
* Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa 

* Your script should take 4 arguments: mysql username, mysql password, database name and state name to search (SQL injection free)
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* You can assume you have one record with the state name to search
* Results must display the states.id
* If no state has the name you searched for, display Not found
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed

### [11. Add a new state](./11-model_state_insert.py)
* Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa 

* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* Print the new states.id after creation
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ ./11-model_state_insert.py root root hbtn_0e_6_usa 
6
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed

### [12. Update a state](./12-model_state_update_id_2.py)
* Write a script that changes the name of a State object from the database hbtn_0e_6_usa 

* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* Change the name of the State where id = 2 to New Mexico
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed

### [13. Delete states](./13-model_state_delete_a.py)
* Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa 

* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ ./13-model_state_delete_a.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
2: New Mexico
4: New York
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed

### [14. Cities in state](./model_city.py)
* Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.

* City class:
    * inherits from Base (imported from model_state)
    * links to the MySQL table cities
    * class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
    * class attribute name that represents a column of a string of 128 characters and can’t be null
    * class attribute state_id that represents a column of an integer, can’t be null and is a foreign key to states.id
* You must use the module SQLAlchemy

Next, write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa:

* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* You must import State and Base from model_state - from model_state import Base, State
* Your script should connect to a MySQL server running on localhost at port 3306
* Results must be sorted in ascending order by cities.id
* Results must be display as they are in the example below (<state name>: (<city id>) <city name>)
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 14-model_city_fetch_by_state.sql
-- Create database hbtn_0e_14_usa, tables states and cities + some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_14_usa;
USE hbtn_0e_14_usa;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/0x0F$ cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
California: (4) Fremont
California: (5) Livermore
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
Texas: (9) Houston
Texas: (10) Austin
New York: (11) New York
Nevada: (12) Las Vegas
Nevada: (13) Reno
Nevada: (14) Henderson
Nevada: (15) Carson City
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed

### [15. City relationship](./relationship_city.py)
* Improve the files model_city.py and model_state.py, and save them as relationship_city.py and relationship_state.py:

    * City class:
    * No change
* State class:
* In addition to previous requirements, the class attribute cities must represent a relationship with the class City. If the State object is deleted, all linked City objects must be automatically deleted. Also, the reference from a City object to his State should be named state
* You must use the module SQLAlchemy

Write a script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)

* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* Your script should connect to a MySQL server running on localhost at port 3306
* You must use the cities relationship for all State objects
* Your code should not be executed when imported
```
guillaume@ubuntu:~/0x0F$ cat 100-relationship_states_cities.sql
-- Create the database hbtn_0e_100_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_100_usa;
USE hbtn_0e_100_usa;

SELECT * FROM states;
SELECT * FROM cities;

guillaume@ubuntu:~/0x0F$ cat 100-relationship_states_cities.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 5: Table 'hbtn_0e_100_usa.states' doesn't exist
guillaume@ubuntu:~/0x0F$ ./100-relationship_states_cities.py root root hbtn_0e_100_usa
guillaume@ubuntu:~/0x0F$ cat 100-relationship_states_cities.sql | mysql -uroot -p
Enter password: 
id  name
1   California
id  name    state_id
1   San Francisco   1
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed

### [16. List relationship](./101-relationship_states_cities_list.py)
* Write a script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa 

* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* The connection to your MySQL server must be to localhost on port 3306
* You must only use one query to the database
* You must use the cities relationship for all State objects
* Results must be sorted in ascending order by states.id and cities.id
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
```
<state id>: <state name>
<tabulation><city id>: <city name>
```
```
guillaume@ubuntu:~/0x0F$ cat 101-relationship_states_cities_list.sql
-- Create states table in hbtn_0e_101_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_101_usa;
USE hbtn_0e_101_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/0x0F$ cat 101-relationship_states_cities_list.sql | mysql -uroot -p
guillaume@ubuntu:~/0x0F$ ./101-relationship_states_cities_list.py root root hbtn_0e_101_usa
1: California
    1: San Francisco
    2: San Jose
    3: Los Angeles
    4: Fremont
    5: Livermore
2: Arizona
    6: Page
    7: Phoenix
3: Texas
    8: Dallas
    9: Houston
    10: Austin
4: New York
    11: New York
5: Nevada
    12: Las Vegas
    13: Reno
    14: Henderson
    15: Carson City
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed

### [17. From city](./102-relationship_cities_states_list.py)
* Write a script that lists all City objects from the database hbtn_0e_101_usa 

* Your script should take 3 arguments: mysql username, mysql password and database name
* You must use the module SQLAlchemy
* Your script should connect to a MySQL server running on localhost at port 3306
* You must use only one query to the database
* You must use the state relationship to access to the State object linked to the City object
* Results must be sorted in ascending order by cities.id
* Results must be displayed as they are in the example below
* Your code should not be executed when imported
```
<city id>: <city name> -> <state name>
```
```
guillaume@ubuntu:~/0x0F$ ./102-relationship_cities_states_list.py root root hbtn_0e_101_usa
1: San Francisco -> California
2: San Jose -> California
3: Los Angeles -> California
4: Fremont -> California
5: Livermore -> California
6: Page -> Arizona
7: Phoenix -> Arizona
8: Dallas -> Texas
9: Houston -> Texas
10: Austin -> Texas
11: New York -> New York
12: Las Vegas -> Nevada
13: Reno -> Nevada
14: Henderson -> Nevada
15: Carson City -> Nevada
guillaume@ubuntu:~/0x0F$ 
```
No test cases needed
---

## Author
* **Robinson Montes** - [mecomonteshbtn](https://github.com/mecomonteshbtn)