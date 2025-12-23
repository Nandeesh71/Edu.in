### Ex. No: 1.a – DDL Commands

**Program:**
```sql
CREATE TABLE emp1 (
    ename VARCHAR2(20),
    eno NUMBER(5),
    addr VARCHAR2(15),
    pho NUMBER(7),
    dept NUMBER(5)
);

DESC emp1;

ALTER TABLE emp1 ADD (salary NUMBER(8,2));

ALTER TABLE emp1 MODIFY (ename VARCHAR2(30));

DESC emp1;

TRUNCATE TABLE emp1;

DROP TABLE emp1;

DESC emp1;
```

**Output:**
```
Table created.

Name        Type
----------  ------------
ENAME       VARCHAR2(20)
ENO         NUMBER(5)
ADDR        VARCHAR2(15)
PHO         NUMBER(7)
DEPT        NUMBER(5)

Table altered.
Table altered.

Name        Type
----------  ------------
ENAME       VARCHAR2(30)
ENO         NUMBER(5)
ADDR        VARCHAR2(15)
PHO         NUMBER(7)
DEPT        NUMBER(5)
SALARY      NUMBER(8,2)

Table truncated.
Table dropped.
ERROR: object emp1 does not exist
```

### Ex. No: 1.b – DML Commands

**Program:**
```sql
CREATE TABLE emp2 (
    empno NUMBER(5),
    empname VARCHAR2(20),
    age NUMBER(3),
    job VARCHAR2(20),
    deptno NUMBER(5),
    salary NUMBER(8,2)
);

INSERT INTO emp2 VALUES (100, 'John', 36, 'Manager', 10, 17500);
INSERT INTO emp2 VALUES (101, 'Smith', 29, 'Clerk', 20, 12000);
INSERT INTO emp2 VALUES (102, 'A', 32, 'Asst Manager', 10, 13500);

SELECT * FROM emp2;

SELECT empno, salary FROM emp2;

SELECT * FROM emp2 WHERE salary > 15000;

UPDATE emp2 SET salary = salary + 500;

UPDATE emp2 SET salary = salary + 500 WHERE age > 35;

DELETE FROM emp2 WHERE deptno = 20;

DELETE FROM emp2;

SELECT * FROM emp2;
```

**Output:**
```
Table created.
3 rows created.

EMPNO EMPNAME   AGE JOB           DEPTNO SALARY
----- --------- --- ------------- ------ ------
  100 John       36 Manager           10  17500
  101 Smith      29 Clerk             20  12000
  102 A          32 Asst Manager      10  13500

EMPNO SALARY
----- ------
  100  17500
  101  12000
  102  13500

EMPNO EMPNAME   AGE JOB           DEPTNO SALARY
----- --------- --- ------------- ------ ------
  100 John       36 Manager           10  17500

3 rows updated.
1 row updated.
1 row deleted.
2 rows deleted.
No rows selected.
```

### Ex. No: 1.c – TCL Commands

**Program:**
```sql
CREATE TABLE account (
    accno NUMBER(5),
    balance NUMBER(10,2)
);

INSERT INTO account VALUES (501, 10000);

COMMIT;

INSERT INTO account VALUES (502, 5000);
SAVEPOINT sp1;

UPDATE account SET balance = balance - 1000 WHERE accno = 501;

SELECT * FROM account;

ROLLBACK TO sp1;

SELECT * FROM account;

INSERT INTO account VALUES (503, 3000);
COMMIT;

SELECT * FROM account;
```

**Output:**
```
Table created.
1 row created.
Commit complete.
1 row created.
Savepoint created.
1 row updated.

ACCNO BALANCE
----- -------
  501   9000
  502   5000

Rollback complete.

ACCNO BALANCE
----- -------
  501  10000
  502   5000

1 row created.
Commit complete.

ACCNO BALANCE
----- -------
  501  10000
  502   5000
  503   3000
```

### Ex. No: 2.a – Basic SQL Queries

**Program:**
```sql
CREATE TABLE student (
    rollno NUMBER(5),
    name VARCHAR2(20),
    dept VARCHAR2(10),
    marks NUMBER(3)
);

INSERT INTO student VALUES (1, 'Ram', 'CSE', 88);
INSERT INTO student VALUES (2, 'Priya', 'ECE', 92);
INSERT INTO student VALUES (3, 'Arun', 'CSE', 75);
INSERT INTO student VALUES (4, 'Meera', 'IT', 95);

SELECT * FROM student;

SELECT name, marks FROM student WHERE dept = 'CSE';

SELECT * FROM student ORDER BY marks DESC;

SELECT dept, AVG(marks) FROM student GROUP BY dept;
```

**Output:**
```
4 rows created.

ROLLNO NAME     DEPT  MARKS
------ -------- ----- -----
     1 Ram      CSE      88
     2 Priya    ECE      92
     3 Arun     CSE      75
     4 Meera    IT       95

NAME     MARKS
-------- -----
Ram         88
Arun        75

ROLLNO NAME     DEPT  MARKS
------ -------- ----- -----
     4 Meera    IT       95
     2 Priya    ECE      92
     1 Ram      CSE      88
     3 Arun     CSE      75

DEPT   AVG(MARKS)
----- ----------
CSE          81.5
ECE            92
IT             95
```

### Ex. No: 2.b – Sub-queries & Nested Queries

**Program:**
```sql
CREATE TABLE department (did NUMBER(3), dname VARCHAR2(15));
CREATE TABLE employee (eid NUMBER(5), ename VARCHAR2(20), did NUMBER(3), salary NUMBER(8,2));

INSERT INTO department VALUES (10, 'HR');
INSERT INTO department VALUES (20, 'IT');

INSERT INTO employee VALUES (1, 'Anu', 10, 45000);
INSERT INTO employee VALUES (2, 'Babu', 20, 60000);
INSERT INTO employee VALUES (3, 'Cathy', 10, 52000);

-- Employees with salary > average
SELECT ename, salary FROM employee 
WHERE salary > (SELECT AVG(salary) FROM employee);

-- Departments having employees with salary > 50000
SELECT dname FROM department 
WHERE did IN (SELECT did FROM employee WHERE salary > 50000);
```

**Output:**
```
ENAME   SALARY
------ -------
Babu     60000
Cathy    52000

DNAME
-------
HR
IT
```

### Ex. No: 2.c – JOIN Operations

**Program:**
```sql
CREATE TABLE cust (cid NUMBER(5), cname VARCHAR2(20));
CREATE TABLE ord (oid NUMBER(5), cid NUMBER(5), amt NUMBER(8,2));

INSERT INTO cust VALUES (1, 'Raj');
INSERT INTO cust VALUES (2, 'Rani');
INSERT INTO cust VALUES (3, 'Somu');

INSERT INTO ord VALUES (101, 1, 5000);
INSERT INTO ord VALUES (102, 2, 3000);
INSERT INTO ord VALUES (103, 4, 2000);

SELECT c.cname, o.amt FROM cust c INNER JOIN ord o ON c.cid = o.cid;

SELECT c.cname, o.amt FROM cust c LEFT JOIN ord o ON c.cid = o.cid;

SELECT c.cname, o.amt FROM cust c RIGHT JOIN ord o ON c.cid = o.cid;
```

**Output:**
```
CNAME   AMT
----- -----
Raj    5000
Rani   3000

CNAME   AMT
----- -----
Raj    5000
Rani   3000
Somu   

CNAME   AMT
----- -----
Raj    5000
Rani   3000
       2000
```

### Ex. No: 3.a – Add Two Numbers (PL/SQL)

**Program:**
```sql
DECLARE
    a NUMBER := 15;
    b NUMBER := 25;
    sum NUMBER;
BEGIN
    sum := a + b;
    DBMS_OUTPUT.PUT_LINE('Sum = ' || sum);
END;
/
```

**Output:**
```
Sum = 40
```

### Ex. No: 3.b – Print n Numbers (FOR Loop)

**Program:**
```sql
DECLARE
    n NUMBER := 6;
BEGIN
    FOR i IN 1..n LOOP
        DBMS_OUTPUT.PUT_LINE(i);
    END LOOP;
END;
/
```

**Output:**
```
1
2
3
4
5
6
```

### Ex. No: 3.c – Print n Numbers (WHILE Loop)

**Program:**
```sql
DECLARE
    n NUMBER := 6;
    i NUMBER := 1;
BEGIN
    WHILE i <= n LOOP
        DBMS_OUTPUT.PUT_LINE(i);
        i := i + 1;
    END LOOP;
END;
/
```

**Output:**
```
1
2
3
4
5
6
```

### Ex. No: 4.a – Debit Amount from Table

**Program:**
```sql
CREATE TABLE bank (accno NUMBER(5), balance NUMBER(10,2));
INSERT INTO bank VALUES (1001, 8000);

DECLARE
    amt NUMBER := 1500;
BEGIN
    UPDATE bank SET balance = balance - amt WHERE accno = 1001;
    COMMIT;
    DBMS_OUTPUT.PUT_LINE('New Balance = ' || (8000 - amt));
END;
/

SELECT * FROM bank;
```

**Output:**
```
New Balance = 6500

ACCNO BALANCE
----- -------
 1001    6500
```

### Ex. No: 4.b – Sum of First N Numbers (Recursion)

**Program:**
```sql
CREATE OR REPLACE FUNCTION sum_n(n NUMBER) RETURN NUMBER IS
BEGIN
    IF n <= 1 THEN RETURN n;
    ELSE RETURN n + sum_n(n-1);
    END IF;
END;
/

BEGIN
    DBMS_OUTPUT.PUT_LINE('Sum = ' || sum_n(10));
END;
/
```

**Output:**
```
Sum = 55
```

### Ex. No: 4.c – Factorial Using Recursion

**Program:**
```sql
CREATE OR REPLACE FUNCTION fact(n NUMBER) RETURN NUMBER IS
BEGIN
    IF n <= 1 THEN RETURN 1;
    ELSE RETURN n * fact(n-1);
    END IF;
END;
/

BEGIN
    DBMS_OUTPUT.PUT_LINE('Factorial of 6 = ' || fact(6));
END;
/
```

**Output:**
```
Factorial of 6 = 720
```

### Ex. No: 5.a – Reverse a String

**Program:**
```sql
DECLARE
    str VARCHAR2(20) := 'DATABASE';
    rev VARCHAR2(20) := '';
    len NUMBER;
BEGIN
    len := LENGTH(str);
    FOR i IN REVERSE 1..len LOOP
        rev := rev || SUBSTR(str, i, 1);
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Reverse = ' || rev);
END;
/
```

**Output:**
```
Reverse = ESABATAD
```

### Ex. No: 5.b – Fibonacci Series

**Program:**
```sql
DECLARE
    n NUMBER := 8;
    a NUMBER := 0;
    b NUMBER := 1;
    c NUMBER;
BEGIN
    DBMS_OUTPUT.PUT_LINE(a);
    DBMS_OUTPUT.PUT_LINE(b);
    FOR i IN 3..n LOOP
        c := a + b;
        DBMS_OUTPUT.PUT_LINE(c);
        a := b;
        b := c;
    END LOOP;
END;
/
```

**Output:**
```
0
1
1
2
3
5
8
13
```

### Ex. No: 5.c – Display Specific Attribute

**Program:**
```sql
CREATE TABLE product (
    pid NUMBER(5),
    pname VARCHAR2(20),
    price NUMBER(8,2)
);

INSERT INTO product VALUES (1, 'Laptop', 55000);
INSERT INTO product VALUES (2, 'Mouse', 500);

SELECT pname FROM product;
```

**Output:**
```
PNAME
-----
Laptop
Mouse
```

### Ex. No: 6 – Banking System (SQL Part)

**Program:**
```sql
CREATE TABLE accounts (
    accno NUMBER(10) PRIMARY KEY,
    name VARCHAR2(30),
    balance NUMBER(10,2)
);

INSERT INTO accounts VALUES (1001, 'Vikram', 10000);

CREATE OR REPLACE PROCEDURE deposit(p_accno NUMBER, p_amt NUMBER) IS
BEGIN
    UPDATE accounts SET balance = balance + p_amt WHERE accno = p_accno;
    DBMS_OUTPUT.PUT_LINE('Deposited. New Balance: ' || (balance + p_amt));
    COMMIT;
END;
/

CREATE OR REPLACE PROCEDURE withdraw(p_accno NUMBER, p_amt NUMBER) IS
    bal NUMBER;
BEGIN
    SELECT balance INTO bal FROM accounts WHERE accno = p_accno;
    IF bal >= p_amt THEN
        UPDATE accounts SET balance = balance - p_amt WHERE accno = p_accno;
        DBMS_OUTPUT.PUT_LINE('Withdrawn. New Balance: ' || (bal - p_amt));
        COMMIT;
    ELSE
        DBMS_OUTPUT.PUT_LINE('Insufficient Balance');
    END IF;
END;
/

EXEC deposit(1001, 2000);
EXEC withdraw(1001, 1000);
SELECT * FROM accounts;
```

**Output:**
```
Deposited. New Balance: 12000
Withdrawn. New Balance: 11000

ACCNO NAME    BALANCE
----- ------- -------
 1001 Vikram    11000
```
