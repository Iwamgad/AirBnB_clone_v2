-- This MySQL script prepares a MySQL server for the project.
-- Create Database if doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create User if doesn't exist and set password to user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all Privileges to user on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant select privileges to user on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;
