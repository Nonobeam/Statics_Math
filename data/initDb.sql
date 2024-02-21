-- initDb.sql

-- Create the housing_database database
CREATE DATABASE HousingDB;
GO

-- Use the housing_database database
USE HousingDB;
GO

-- Create a table to store housing data
CREATE TABLE Housing (
    id INT IDENTITY(1,1) PRIMARY KEY,
    city NVARCHAR(100),
    bedrooms INT,
    bathrooms INT,
    area FLOAT,  -- in square feet
    price FLOAT   -- in dollars
);
GO

-- Insert sample housing data into the table
INSERT INTO housing (city, bedrooms, bathrooms, area, price) VALUES
    ('New York', 3, 2, 1500, 500000),
    ('Los Angeles', 2, 1, 1200, 400000),
    ('Chicago', 4, 3, 2000, 600000),
    ('Houston', 3, 2, 1800, 450000),
    ('Phoenix', 3, 2, 1600, 380000),
    ('Philadelphia', 2, 1, 1300, 410000),
    ('San Antonio', 4, 3, 2200, 620000),
    ('San Diego', 3, 2, 1700, 520000),
    ('Dallas', 4, 3, 2100, 590000),
    ('San Jose', 3, 2, 1600, 630000),
    ('Austin', 2, 2, 1400, 480000),
    ('Jacksonville', 3, 2, 1700, 410000),
    ('Fort Worth', 4, 3, 2000, 550000),
    ('Columbus', 3, 2, 1600, 420000),
    ('Charlotte', 2, 1, 1200, 370000),
    ('San Francisco', 3, 2, 1800, 850000),
    ('Indianapolis', 4, 3, 2100, 480000),
    ('Seattle', 3, 2, 1600, 720000),
    ('Denver', 2, 2, 1500, 600000),
    ('Washington', 3, 2, 1700, 780000);
