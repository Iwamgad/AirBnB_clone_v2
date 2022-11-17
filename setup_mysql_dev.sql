-- This mysql script prepares a MySQL server for the project.

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create Database if doesn't Exist and set password for user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all Privileges to user on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant select privileges to user on performa_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Flush privilages
FLUSH PRIVILEGES;
