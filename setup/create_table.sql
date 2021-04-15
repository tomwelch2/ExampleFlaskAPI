CREATE TABLE IF NOT EXISTS company.employees(emp_id INT PRIMARY KEY AUTO_INCREMENT, firstname VARCHAR(50), surname VARCHAR(50),
salary INT, branch_id INT) COMMENT = "Table to be used in API" ENGINE = INNODB;
