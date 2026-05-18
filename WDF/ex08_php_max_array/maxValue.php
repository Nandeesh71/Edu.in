# Ex 08 – PHP Function to Find Maximum Value in an Array

## AIM
To write a PHP function that accepts an array of numbers and returns the maximum value.

## Procedure
1. Create `maxarray.php`.
2. Define `findMaxValue($numbers)` that checks if the array is empty first.
3. Initialize `$max` with the first element.
4. Loop through the array using `foreach` and update `$max` if a larger value is found.
5. Return `$max` and display the result.

## Output
```
Array: 12, 45, 7, 99, 34
Maximum Value: 99
```






<?php
function findMaxValue($numbers) {
    // Check if the array is empty
    if (empty($numbers)) {
        return null;
    }

    // Initialize the max variable to the first value in the array
    $max = $numbers[0];

    // Loop through the array
    foreach ($numbers as $number) {
        // If current number is greater than max, update max
        if ($number > $max) {
            $max = $number;
        }
    }

    return $max;
}

// Test the function with a sample array
$sampleArray = [12, 45, 7, 99, 34];
echo "Array: " . implode(", ", $sampleArray) . "<br>";
echo "The maximum value is: " . findMaxValue($sampleArray);
?>
