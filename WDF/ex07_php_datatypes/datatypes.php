# Ex 07 – PHP Variables, Data Types, and Constants

## AIM
To declare and initialize PHP variables using different data types (integer, string, float, Boolean) and define a constant using `define()`.

## Procedure
1. Create `variables.php`.
2. Declare variables for each data type.
3. Use `define()` to create a constant.
4. Use `echo` to display all values.
5. Run using PHP CLI or a local server.

### PHP Data Types Used
| Type | Example |
|------|---------|
| Integer | `$age = 25` |
| String | `$name = "John Doe"` |
| Float | `$salary = 45000.75` |
| Boolean | `$isEmployed = true` |
| Constant | `define("COMPANY_NAME", "...")` |

## Output
```
Name: John Doe
Age: 25
Salary: 45000.75
Employed: Yes
Company: Tech Solutions Ltd
```







<?php
// Integer data type
$age = 25;

// String data type
$name = "John Doe";

// Float (double) data type
$salary = 45000.75;

// Boolean data type
$isEmployed = true;

// Defining a constant
define("COMPANY_NAME", "Tech Solutions Ltd");

// Displaying values
echo "Name: $name <br>";
echo "Age: $age <br>";
echo "Salary: $salary <br>";
echo "Employed: " . ($isEmployed ? "Yes" : "No") . "<br>";
echo "Company: " . COMPANY_NAME;
?>
