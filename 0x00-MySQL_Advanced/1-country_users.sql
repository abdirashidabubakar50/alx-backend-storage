-- create table users wth the following requirements
-- id- never null, auto increment and primary key
-- email - string(255 characters)  never null and unique
-- name - string(255 characters)
-- country, enumeration of countries: US, CO AND IN, never null (=default wil be the first element of the enumeration, here US)

CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);