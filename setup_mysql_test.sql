-- The script that prepares a MySQL server for AirBnB clone v2
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant hbnb_test all privileges on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant select privileges on performance_schema
GRANT SELECT ON  performance_schema.* TO 'hbnb_test'@'localhost';
