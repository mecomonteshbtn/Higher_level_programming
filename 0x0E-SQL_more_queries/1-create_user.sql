-- Create an user with password
-- DDL query to create a MySQL user with pasword
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- add privileges to user
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
