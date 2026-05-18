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
