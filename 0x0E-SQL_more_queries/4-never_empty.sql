-- create id not null
-- DDL query to create table with id initialized in 1
CREATE TABLE IF NOT EXISTS id_not_null(
id INT DEFAULT 1, name VARCHAR(256) NOT NULL );
