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
