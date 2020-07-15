-- Create table adding FOREING KEY
-- DDL query to create state_id with a FOREING KEY 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- set database
USE hbtn_0d_usa;
-- create table if doesnt exist
CREATE TABLE IF NOT EXISTS cities(
id INT NOT NULL AUTO_INCREMENT UNIQUE,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (state_id) REFERENCES states(id)
);
