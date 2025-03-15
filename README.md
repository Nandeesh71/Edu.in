# Print(" Thank Me Later ... ! ") 



1. Find Minimum in a List
def find_minimum(lst):
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

numbers = [12, 5, 8, 20, 3, 7]
min_value = find_minimum(numbers)
print("The minimum value in the list is:", min_value)
Output:
The minimum value in the list is: 3
________________________________________
2. Insert a Card in a Sorted List
def insert_card(sorted_cards, new_card):
    for i in range(len(sorted_cards)):
        if sorted_cards[i] > new_card:
            sorted_cards.insert(i, new_card)
            return sorted_cards
    sorted_cards.append(new_card)
    return sorted_cards

sorted_cards = [2, 4, 6, 8, 10]
print("Sorted Cards:", sorted_cards)
new_card = int(input("Enter the card to insert: "))
updated_cards = insert_card(sorted_cards, new_card)
print("Updated Sorted Cards:", updated_cards)
Output:
Sorted Cards: [2, 4, 6, 8, 10]  
Enter the card to insert: 5  
Updated Sorted Cards: [2, 4, 5, 6, 8, 10]  
________________________________________
3. BMI Calculation
def BMI_Calc(weight, height):
    return weight / (height ** 2)

persons = []
for i in range(5):
    height = float(input("Enter height (in meters): "))
    weight = float(input("Enter weight (in kilograms): "))
    persons.append((height, weight))

for i, (height, weight) in enumerate(persons, 1):
    bmi = BMI_Calc(weight, height)
    print(f"Person {i} - Height: {height} m, Weight: {weight} kg, BMI: {bmi:.2f}")
Output:
Person 1 - Height: 1.75 m, Weight: 60.0 kg, BMI: 19.59  
Person 2 - Height: 1.60 m, Weight: 70.0 kg, BMI: 27.34  
Person 3 - Height: 1.85 m, Weight: 65.0 kg, BMI: 18.99  
________________________________________
4. Simple Data Types Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print("Name:", name)
print("Age:", age)
print("Height:", height)
Output:
Enter your name: ANU  
Enter your age: 25  
Enter your height: 5.8  

Name: ANU  
Age: 25  
Height: 5.8  
________________________________________
5. Find Square and Cube of a Number
num = float(input("Enter a number: "))
square = num ** 2
cube = num ** 3
print(f"The square of {num} is {square}")
print(f"The cube of {num} is {cube}")
Output:
Enter a number: 3  
The square of 3.0 is 9.0  
The cube of 3.0 is 27.0  
________________________________________
6. Find Roots of a Quadratic Equation
import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c
root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

print(f"The roots of the quadratic equation are: {root1} and {root2}")
Output:
Enter the coefficient a: 1  
Enter the coefficient b: 2  
Enter the coefficient c: 5  
The roots of the quadratic equation are: (-1+2j) and (-1-2j)  
________________________________________
7. Find Square Root and Cube Root
import math

num = float(input("Enter a number: "))
square_root = math.sqrt(num)
cube_root = num ** (1/3)

print(f"Square root of {num}: {square_root}")
print(f"Cube root of {num}: {cube_root}")
Output:
Enter a number: 27  
Square root of 27.0: 5.196152422706632  
Cube root of 27.0: 3.0  
________________________________________
8. Calculate Simple Interest
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))

simple_interest = calculate_simple_interest(principal, rate, time)
print(f"Simple Interest: {simple_interest}")
Output:
Enter the principal amount: 1000  
Enter the rate of interest: 5  
Enter the time period in years: 2  
Simple Interest: 100.0  
________________________________________
9. Determine Age Group Based on Age
age = int(input("Enter your age: "))

if age <= 1:
    age_group = "Infant"
elif age <= 12:
    age_group = "Children"
elif age <= 17:
    age_group = "Adolescents"
elif age <= 59:
    age_group = "Adults"
else:
    age_group = "Older adults"

print(f"Age group: {age_group}")
Output:
Enter your age: 25  
Age group: Adults  
________________________________________
10. Countdown from a Number
num = int(input("Enter a number to start the countdown: "))

while num >= 0:
    print(num)
    num -= 1
Output:
Enter a number to start the countdown: 5  
5  
4  
3  
2  
1  
0  
________________________________________
11. Print Pascal's Triangle
def print_pascals_triangle(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")
        num = 1
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        print()

rows = int(input("Enter the number of rows for Pascal's Triangle: "))
print_pascals_triangle(rows)
Output:
Enter the number of rows for Pascal's Triangle: 5  
    1  
   1 1  
  1 2 1  
 1 3 3 1  
1 4 6 4 1  
________________________________________
12. Print Multiplication Table
num = int(input("Enter a number to print its multiplication table: "))

print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
Output:
Enter a number to print its multiplication table: 5  
5 x 1 = 5  
5 x 2 = 10  
5 x 3 = 15  
...  
5 x 10 = 50  
________________________________________
13. Display Favorite Actor/Actress with 'Lucky' in the String
favorite_actor = "Leonardo DiCaprio"
print(f"My favorite actor is {favorite_actor}, and I consider myself lucky to admire their work.")
Output:
My favorite actor is Leonardo DiCaprio, and I consider myself lucky to admire their work.
________________________________________
14. Print the Current Date in "Day/Month/Year" Format
from datetime import datetime

today = datetime.today()
print(f"Today is {today.day}/{today.month}/{today.year}")
Output:
Today is 18/3/2025
________________________________________
15. Split an Article into Phrases
import re

def split_article_into_phrases(article):
    phrases = re.split(r'[.!?]', article)
    phrases = [phrase.strip() for phrase in phrases if phrase.strip()]
    return phrases

article = """Python is a great programming language. It is versatile and easy to learn!
Many people use Python for web development, data analysis, and automation.
Are you ready to learn Python? It will help you in various fields of technology."""

phrases = split_article_into_phrases(article)
for i, phrase in enumerate(phrases, 1):
    print(f"Phrase {i}: {phrase}")
Output:
Phrase 1: Python is a great programming language  
Phrase 2: It is versatile and easy to learn  
Phrase 3: Many people use Python for web development, data analysis, and automation  
Phrase 4: Are you ready to learn Python  
Phrase 5: It will help you in various fields of technology  
________________________________________
16. Read a File and Display Contents with Line Numbers
try:
    with open('file.txt', 'r') as file:
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1
except FileNotFoundError:
    print("Error: The file 'file.txt' was not found.")
Output:
Line 1: Hello, this is line 1.  
Line 2: This is line 2.  
Line 3: Here comes line 3.  
________________________________________
17. Read and Sort Student Records from a File
try:
    with open('students.txt', 'r') as file:
        records = [line.strip().split(',') for line in file]
        sorted_records = sorted(records, key=lambda x: x[0])

    print("Student Records in Sorted Order by Name:")
    for name, age in sorted_records:
        print(f"Name: {name}, Age: {age}")
except FileNotFoundError:
    print("Error: The file 'students.txt' was not found.")
Output:
Student Records in Sorted Order by Name:  
Name: Alice, Age: 20  
Name: Bob, Age: 19  
Name: Charlie, Age: 21  
________________________________________
18. Perform Matrix Operations Using NumPy
import numpy as np

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

addition = matrix1 + matrix2
multiplication = np.dot(matrix1, matrix2)
transpose = np.transpose(matrix1)

print("Matrix Addition:\n", addition)
print("Matrix Multiplication:\n", multiplication)
print("Transpose of Matrix 1:\n", transpose)
________________________________________
19. Perform DataFrame Operations Using Pandas
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [24, 27, 22],
        'Salary': [50000, 60000, 45000]}

df = pd.DataFrame(data)
df['Bonus'] = df['Salary'] * 0.1

print("DataFrame after adding Bonus column:\n", df)
________________________________________
20. Visualizing Dataset Using Matplotlib
import matplotlib.pyplot as plt
import pandas as pd

data = {'Year': [2017, 2018, 2019, 2020, 2021],
        'Sales': [250, 340, 290, 410, 460]}
df = pd.DataFrame(data)

plt.plot(df['Year'], df['Sales'], marker='o', label='Sales')
plt.title('Yearly Sales Trend')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.legend()
plt.grid()
plt.show()
