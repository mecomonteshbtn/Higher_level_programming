-- create a table unique_id
-- DDL query to create a table with default value 1 and must be unique
CREATE TABLE IF NOT EXISTS unique_id(
id INT DEFAULT 1 UNIQUE, name VARCHAR(256) NOT NULL);
