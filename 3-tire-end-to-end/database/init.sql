-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS appdb;

-- Use the database
USE appdb;

-- Create a sample table: users
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO users (name, email) VALUES
('Admin User', 'admin@example.com'),
('Test User', 'test@example.com'),
('John Doe', 'john@example.com');
