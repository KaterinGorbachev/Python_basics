DROP DATABASE IF EXISTS examen_users; 
CREATE DATABASE examen_users;
USE examen_users; 
CREATE TABLE users(id INTEGER AUTO_INCREMENT PRIMARY KEY, email VARCHAR(100), password_hash text); 
 