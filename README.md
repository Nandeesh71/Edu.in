Warning
⚠️ Create and use the schema before running any SQL commands.


``` sql
CREATE DATABASE DBMS_Lab_Exam;
USE DBMS_Lab_Exam;
```
⚠️ Skipping this step will cause errors.


-------------------------------------------------------------------------------------------------------------------------------------------------------

🤝 https://chatgpt.com/s/t_694ad9ce2c188191bb418b85abf26ead 🖇️

------------------------------------------------------------------------------------------------------------------------------------------------------

# Module I: Database Design
## a) Data Definition Language - Create, Describe, Alter, Truncate, Drop
### i) Create the employee table with the following columns (EMP ID, EMP NAME, EMP AGE)
**SQL Code:**
```sql
CREATE TABLE employee (
    EMP_ID INT PRIMARY KEY,
    EMP_NAME VARCHAR(50),
    EMP_AGE INT
);
```
**Expected Output:**
Table created successfully.
### ii) Use a command to describe the structure of the employee’s table.
**SQL Code:**
```sql
DESC employee;
```
**Expected Output:**
```
Field     Type        Null Key Default Extra
EMP_ID    int         NO   PRI NULL    
EMP_NAME  varchar(50) YES      NULL    
EMP_AGE   int         YES      NULL    
```
### iii) Write an SQL statement to alter the employees table to add a new column salary.
**SQL Code:**
```sql
ALTER TABLE employee ADD salary DECIMAL(10,2);
```
**Expected Output:**
Table altered successfully.
### iv) Use a command to truncate the employees table, removing all rows but keeping the structure intact.
**SQL Code:**
```sql
TRUNCATE TABLE employee;
```
**Expected Output:**
Table truncated successfully (all rows removed, structure remains).
### v) Write a command to drop the employees table completely from the database.
**SQL Code:**
```sql
DROP TABLE employee;
```
**Expected Output:**
Table dropped successfully.
## b) Data Manipulation Language - Insert, Select, Update, Delete
**Create Table and Sample Data (for demonstration):**
```sql
CREATE TABLE student (
    ID INT PRIMARY KEY,
    NAME VARCHAR(50),
    GRADE INT
);
INSERT INTO student (ID, NAME, GRADE) VALUES (1, 'John Doe', 85);
```
### i) Write an SQL command to insert a new student with (ID, NAME and GRADE)
**SQL Code:**
```sql
INSERT INTO student (ID, NAME, GRADE) VALUES (2, 'Alice Smith', 90);
```
**Expected Output:**
1 row inserted.
### ii) Write a select query to retrieve all records from the student’s table.
**SQL Code:**
```sql
SELECT * FROM student;
```
**Expected Output:**
```
ID | NAME       | GRADE
---|------------|------
1  | John Doe   | 85
2  | Alice Smith| 90
```
### iii) Write an SQL command to update the grade of the student with ID.
**SQL Code:**
```sql
UPDATE student SET GRADE = 95 WHERE ID = 1;
```
**Expected Output:**
1 row updated.
### iv) Write an SQL command to delete the student record with their NAME.
**SQL Code:**
```sql
DELETE FROM student WHERE NAME = 'Alice Smith';
```
**Expected Output:**
1 row deleted.
## c) Transaction Control Language - Commit, Rollback, and Savepoint
**Create Table and Initial Setup (for demonstration):**
```sql
CREATE TABLE student (
    ID INT PRIMARY KEY,
    NAME VARCHAR(50)
);
```
### i) Insert a new ID and name and Set a SAVEPOINT after the insertion.
**SQL Code:**
```sql
START TRANSACTION;
INSERT INTO student (ID, NAME) VALUES (1, 'John Doe');
SAVEPOINT sp1;
```
**Expected Output:**
1 row inserted.
Savepoint created.
### ii) Insert another ID and name. Note that the second insertion was a mistake, so ROLLBACK to the savepoint.
**SQL Code:**
```sql
INSERT INTO student (ID, NAME) VALUES (2, 'Alice Smith');
ROLLBACK TO sp1;
```
**Expected Output:**
1 row inserted.
Rollback complete (second insert undone).
### iii) COMMIT the transaction to make the first insertion permanent in the database.
**SQL Code:**
```sql
COMMIT;
```
**Expected Output:**
Commit complete.

-------------------------------------------------------------------------------------------------------------------------------------------------------

# Module II: Relational Databases
## Database Querying:
## a) Write simple SQL queries to perform the following
**Create Table and Sample Data (for demonstration):**
```sql
CREATE TABLE student (
    ID INT PRIMARY KEY,
    NAME VARCHAR(50),
    GRADE INT
);
INSERT INTO student (ID, NAME, GRADE) VALUES (1, 'John', 85);
INSERT INTO student (ID, NAME, GRADE) VALUES (2, 'Alice', 95);
INSERT INTO student (ID, NAME, GRADE) VALUES (3, 'Bob', 70);
```
### i) Retrieve all the records from the student’s table.
**SQL Code:**
```sql
SELECT * FROM student;
```
**Expected Output:**
```
ID | NAME  | GRADE
---|-------|------
1  | John  | 85
2  | Alice | 95
3  | Bob   | 70
```
### ii) Display only the name and grade of each student.
**SQL Code:**
```sql
SELECT NAME, GRADE FROM student;
```
**Expected Output:**
```
NAME  | GRADE
------|------
John  | 85
Alice | 95
Bob   | 70
```
### iii) Select all students who have scored more than 80.
**SQL Code:**
```sql
SELECT * FROM student WHERE GRADE > 80;
```
**Expected Output:**
```
ID | NAME  | GRADE
---|-------|------
1  | John  | 85
2  | Alice | 95
```
### iv) Display all student records sorted by grade in descending order.
**SQL Code:**
```sql
SELECT * FROM student ORDER BY GRADE DESC;
```
**Expected Output:**
```
ID | NAME  | GRADE
---|-------|------
2  | Alice | 95
1  | John  | 85
3  | Bob   | 70
```
### v) Retrieve only the first two records from the table.
**SQL Code:**
```sql
SELECT * FROM student LIMIT 2;
```
**Expected Output:**
```
ID | NAME  | GRADE
---|-------|------
1  | John  | 85
2  | Alice | 95
```
## b) Nested Queries
**Create Tables and Sample Data (for demonstration):**
```sql
CREATE TABLE employee (
    EMP_ID INT PRIMARY KEY,
    EMP_NAME VARCHAR(50),
    SALARY INT,
    DEPT_ID INT
);
CREATE TABLE departments (
    DEPT_ID INT PRIMARY KEY,
    DEPT_NAME VARCHAR(50)
);
INSERT INTO employee (EMP_ID, EMP_NAME, SALARY, DEPT_ID) VALUES (1, 'John', 50000, 10);
INSERT INTO employee (EMP_ID, EMP_NAME, SALARY, DEPT_ID) VALUES (2, 'Alice', 60000, 20);
INSERT INTO employee (EMP_ID, EMP_NAME, SALARY, DEPT_ID) VALUES (3, 'Bob', 45000, 10);
INSERT INTO employee (EMP_ID, EMP_NAME, SALARY, DEPT_ID) VALUES (4, 'Eve', 70000, 30);
INSERT INTO departments (DEPT_ID, DEPT_NAME) VALUES (10, 'HR');
INSERT INTO departments (DEPT_ID, DEPT_NAME) VALUES (20, 'IT');
INSERT INTO departments (DEPT_ID, DEPT_NAME) VALUES (30, 'Finance');
```
### i) Retrieve the employee(s) who earn the highest salary in the company using a subquery.
**SQL Code:**
```sql
SELECT * FROM employee WHERE SALARY = (SELECT MAX(SALARY) FROM employee);
```
**Expected Output:**
```
EMP_ID | EMP_NAME | SALARY | DEPT_ID
-------|----------|--------|--------
4      | Eve      | 70000  | 30
```
### ii) Display the names and salaries of employees whose salary is above the average salary of all employees.
**SQL Code:**
```sql
SELECT EMP_NAME, SALARY FROM employee WHERE SALARY > (SELECT AVG(SALARY) FROM employee);
```
**Expected Output (average ~56250):**
```
EMP_NAME | SALARY
---------|-------
Alice    | 60000
Eve      | 70000
```
### iii) Find the department(s) where the lowest salary is paid, using a nested query
**SQL Code:**
```sql
SELECT DEPT_NAME FROM departments WHERE DEPT_ID IN (
    SELECT DEPT_ID FROM employee GROUP BY DEPT_ID HAVING MIN(SALARY) = (SELECT MIN(SALARY) FROM employee)
);
```
**Expected Output:**
```
DEPT_NAME
---------
HR
```
### iv) List all employees whose department_id is found in a list of departments where at least one employee earns more than 100000, using a multi-row subquery
**SQL Code (assuming Eve's salary updated to 120000 for demo):**
```sql
UPDATE employee SET SALARY = 120000 WHERE EMP_ID = 4;
SELECT * FROM employee WHERE DEPT_ID IN (SELECT DEPT_ID FROM employee WHERE SALARY > 100000);
```
**Expected Output:**
```
EMP_ID | EMP_NAME | SALARY | DEPT_ID
-------|----------|--------|--------
4      | Eve      | 120000 | 30
```
## c) Joins (Inner Join, Left Join, Right Join, Full Join, Cross Join )
**Create Tables and Sample Data (using the same from above):**
(Already created in b) above.)
### i) Write a SQL query to list the names of all employees along with their department names, only for those employees who have a corresponding department in the departments table. Use an INNER JOIN.
**SQL Code:**
```sql
SELECT e.EMP_NAME, d.DEPT_NAME
FROM employee e INNER JOIN departments d ON e.DEPT_ID = d.DEPT_ID;
```
**Expected Output:**
```
EMP_NAME | DEPT_NAME
---------|----------
John     | HR
Bob      | HR
Alice    | IT
Eve      | Finance
```
### ii) Write a SQL query to retrieve a list of all employees and their department names. If an employee does not belong to any department, show the department name as NULL. Use a LEFT JOIN.
**SQL Code:**
```sql
SELECT e.EMP_NAME, d.DEPT_NAME
FROM employee e LEFT JOIN departments d ON e.DEPT_ID = d.DEPT_ID;
```
**Expected Output:**
```
EMP_NAME | DEPT_NAME
---------|----------
John     | HR
Bob      | HR
Alice    | IT
Eve      | Finance
```
(If an employee has no dept, DEPT_NAME would be NULL.)
### iii) Write a SQL query to list all departments along with the names of employees working in those departments. If a department has no employees, display NULL for employee names. Use a RIGHT JOIN.
**SQL Code:**
```sql
SELECT e.EMP_NAME, d.DEPT_NAME
FROM employee e RIGHT JOIN departments d ON e.DEPT_ID = d.DEPT_ID;
```
**Expected Output:**
```
EMP_NAME | DEPT_NAME
---------|----------
John     | HR
Bob      | HR
Alice    | IT
Eve      | Finance
```
(If a dept has no employees, EMP_NAME NULL.)
### iv) Write a SQL query to list all employees and all departments, even if some employees are not assigned to a department and some departments have no employees. Use a FULL OUTER JOIN.
**SQL Code:**
```sql
SELECT e.EMP_NAME, d.DEPT_NAME
FROM employee e LEFT JOIN departments d ON e.DEPT_ID = d.DEPT_ID
UNION
SELECT e.EMP_NAME, d.DEPT_NAME
FROM employee e RIGHT JOIN departments d ON e.DEPT_ID = d.DEPT_ID;
```
**Expected Output:**
All combinations with NULLs for non-matches.
### v) Write a SQL query to list all possible combinations of employee names and department names from the employees and departments tables. Use a CROSS JOIN
**SQL Code:**
```sql
SELECT e.EMP_NAME, d.DEPT_NAME
FROM employee e CROSS JOIN departments d;
```
**Expected Output:**
12 rows (4 employees x 3 depts), all possible pairs.

-------------------------------------------------------------------------------------------------------------------------------------------------------

# Module III: Transactions

These use PL/SQL blocks (Oracle-style).

## a) Write a SQL program for adding two numbers and displaying the sum.

**PL/SQL Code:**
```sql
DECLARE
    num1 NUMBER := 5;
    num2 NUMBER := 10;
    sum_num NUMBER;
BEGIN
    sum_num := num1 + num2;
    DBMS_OUTPUT.PUT_LINE('Sum: ' || sum_num);
END;
```

**Expected Output:**  
Sum: 15

## b) Write a SQL program to print a series of “n” numbers using for loop.

**PL/SQL Code:**
```sql
DECLARE
    n NUMBER := 5;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Series using FOR loop:');
    FOR i IN 1..n LOOP
        DBMS_OUTPUT.PUT_LINE(i);
    END LOOP;
END;
```

**Expected Output:**  
Series using FOR loop:  
1  
2  
3  
4  
5

## c) Write a SQL program to print a series of “n” numbers using while loop.

**PL/SQL Code:**
```sql
DECLARE
    n NUMBER := 5;
    i NUMBER := 1;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Series using WHILE loop:');
    WHILE i <= n LOOP
        DBMS_OUTPUT.PUT_LINE(i);
        i := i + 1;
    END LOOP;
END;
```

**Expected Output:**  
Series using WHILE loop:  
1  
2  
3  
4  
5

-------------------------------------------------------------------------------------------------------------------------------------------------------

# Module IV: Implementation Techniques

## List of Experiments:

**Create Table and Sample Data for a) (account table):**
```sql
CREATE TABLE account (
    ACC_ID NUMBER PRIMARY KEY,
    BALANCE NUMBER
);

INSERT INTO account (ACC_ID, BALANCE) VALUES (1, 1000);
COMMIT;
```

## a) Write a SQL program for debiting an amount from an entry in a table

**PL/SQL Code:**
```sql
DECLARE
    acc_id NUMBER := 1;
    debit_amount NUMBER := 200;
    new_balance NUMBER;
BEGIN
    UPDATE account SET BALANCE = BALANCE - debit_amount WHERE ACC_ID = acc_id;
    COMMIT;
    SELECT BALANCE INTO new_balance FROM account WHERE ACC_ID = acc_id;
    DBMS_OUTPUT.PUT_LINE('Debited ' || debit_amount || '. New balance: ' || new_balance);
END;
```

**Expected Output:**  
Debited 200. New balance: 800

## b) Write a SQL program to determine the sum of a series of n numbers.

**PL/SQL Code:**
```sql
DECLARE
    n NUMBER := 5;
    total_sum NUMBER := 0;
BEGIN
    FOR i IN 1..n LOOP
        total_sum := total_sum + i;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Sum of first ' || n || ' numbers: ' || total_sum);
END;
```

**Expected Output:**  
Sum of first 5 numbers: 15

## c) Write a SQL program to determine the factorial of the given number.

**PL/SQL Code:**
```sql
DECLARE
    n NUMBER := 5;
    factorial NUMBER := 1;
BEGIN
    FOR i IN 1..n LOOP
        factorial := factorial * i;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Factorial of ' || n || ': ' || factorial);
END;
```

**Expected Output:**  
Factorial of 5: 120

-------------------------------------------------------------------------------------------------------------------------------------------------------

# Module V: Database Models

## List of Experiments:

**Create Table and Sample Data for c) (employee table, reusing from Module II):**
```sql
-- Assuming employee table from Module II
INSERT INTO employee (EMP_ID, EMP_NAME, SALARY, DEPT_ID) VALUES (1, 'John', 50000, 10);
COMMIT;
```

## a) Write a SQL program for reversing a string using the for loop.

**PL/SQL Code:**
```sql
DECLARE
    input_str VARCHAR2(20) := 'Hello';
    reversed_str VARCHAR2(20) := '';
    str_len NUMBER;
BEGIN
    str_len := LENGTH(input_str);
    FOR i IN REVERSE 1..str_len LOOP
        reversed_str := reversed_str || SUBSTR(input_str, i, 1);
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Reversed string: ' || reversed_str);
END;
```

**Expected Output:**  
Reversed string: olleH

## b) Write a SQL program to implement Fibonacci series.

**PL/SQL Code:**
```sql
DECLARE
    n NUMBER := 8;
    a NUMBER := 0;
    b NUMBER := 1;
    c NUMBER;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Fibonacci series up to ' || n || ' terms:');
    DBMS_OUTPUT.PUT_LINE(a);
    DBMS_OUTPUT.PUT_LINE(b);
    FOR i IN 3..n LOOP
        c := a + b;
        DBMS_OUTPUT.PUT_LINE(c);
        a := b;
        b := c;
    END LOOP;
END;
```

**Expected Output:**  
Fibonacci series up to 8 terms:  
0  
1  
1  
2  
3  
5  
8  
13

## c) Write a SQL program for displaying a particular attribute from a table.

**PL/SQL Code:**
```sql
BEGIN
    DBMS_OUTPUT.PUT_LINE('Employee Names:');
    FOR rec IN (SELECT EMP_NAME FROM employee) LOOP
        DBMS_OUTPUT.PUT_LINE(rec.EMP_NAME);
    END LOOP;
END;
```

**Expected Output:**  
Employee Names:  
John  
Alice  
Bob  
Eve

-------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------

# Module VI: Advanced Topics

## List of Experiments:

## a) Mini Project (Banking System) Connect Oracle Database from Visual Basic for Banking System.

This involves a simple Visual Basic .NET application connecting to Oracle for banking operations (e.g., view balance, deposit, withdraw). Assume Oracle.DataAccess.Client library is used.

**Create Table for Demonstration (Oracle Side):**
```sql
CREATE TABLE account (
    ACC_ID NUMBER PRIMARY KEY,
    BALANCE NUMBER
);

INSERT INTO account (ACC_ID, BALANCE) VALUES (1, 1000);
COMMIT;
```

**VB.NET Code Snippet (Form with buttons: Connect, View Balance, Deposit):**
```vb
Imports Oracle.ManagedDataAccess.Client

Public Class BankingForm
    Private con As OracleConnection

    Private Sub ConnectButton_Click(sender As Object, e As EventArgs) Handles ConnectButton.Click
        con = New OracleConnection("User Id=your_username;Password=your_password;Data Source=your_oracle_db")
        Try
            con.Open()
            MsgBox("Connected to Oracle!")
        Catch ex As Exception
            MsgBox("Connection Error: " & ex.Message)
        End Try
    End Sub

    Private Sub ViewBalanceButton_Click(sender As Object, e As EventArgs) Handles ViewBalanceButton.Click
        If con.State = ConnectionState.Open Then
            Dim cmd As New OracleCommand("SELECT BALANCE FROM account WHERE ACC_ID = 1", con)
            Dim balance As Object = cmd.ExecuteScalar()
            MsgBox("Current Balance: " & balance.ToString())
        Else
            MsgBox("Please connect first!")
        End If
    End Sub

    Private Sub DepositButton_Click(sender As Object, e As EventArgs) Handles DepositButton.Click
        If con.State = ConnectionState.Open Then
            Dim amount As Decimal = 100  ' Example amount; use input in real app
            Dim cmd As New OracleCommand("UPDATE account SET BALANCE = BALANCE + :amt WHERE ACC_ID = 1", con)
            cmd.Parameters.Add("amt", OracleDbType.Decimal).Value = amount
            cmd.ExecuteNonQuery()
            con.Commit()  ' Assuming autocommit off
            MsgBox("Deposited " & amount & ". New balance: " & (1000 + amount))
        Else
            MsgBox("Please connect first!")
        End If
    End Sub
End Class
```

**Expected Output:**  
- On Connect: "Connected to Oracle!" message.  
- On View Balance: "Current Balance: 1000" (or updated value).  
- On Deposit: "Deposited 100. New balance: 1100" message.
