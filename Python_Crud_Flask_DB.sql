-- Create the database if it does not exist
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'db_PythonCrud')
BEGIN
    CREATE DATABASE db_PythonCrud;
END

USE db_PythonCrud;

-- Create the 'students' table
CREATE TABLE students (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL
);


-- Insert initial data into the 'students' table
INSERT INTO students (name, email, phone) VALUES
('Parwiz', 'parwiz.f@gmail.com', '009378976767'),
('John Doe', 'johndoe@gmail.com', '999999999'),
('Karimja', 'ka@gmail.com', '7333392'),
('Jamal', 'ja@gmail.com', '3434343'),
('Nawid', 'na@gmail.com', '343434'),
('Tom Logan', 'Tom@gmail.com', '7347374347'),
('Tom Logan', 'tom@gmail.com', '11111111111'),
('Fawad', 'fa@gmail.com', '347374837483'),
('Wahid', 'wa@gmail.com', '4354354345');

Select * from students
-- Optional: Drop the 'students_new' table if it exists
IF OBJECT_ID('students_new', 'U') IS NOT NULL
BEGIN
    DROP TABLE students_new;
END

-- Create the new 'students' table with an identity column
CREATE TABLE students_new (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL
);
Select * from students_new
-- Copy data from the old 'students' table to the new one
INSERT INTO students_new (name, email, phone)
SELECT name, email, phone FROM students;

-- Drop the old 'students' table
DROP TABLE students;

-- Rename 'students_new' to 'students'
EXEC sp_rename 'students_new', 'students';
