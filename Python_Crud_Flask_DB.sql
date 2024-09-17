create database Python_Flask_Crud_db

use Python_Flask_Crud_db

CREATE TABLE nurse (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10)
);

Select * from  nurse

CREATE TABLE patient (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    nurse_id INT,
    FOREIGN KEY (nurse_id) REFERENCES nurse(id)
);

Select * from  patient