#Q1. Write a program to check if a given number is Positive, Negative or Zero.
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#Q2. Write a program to check if a given number is odd or even.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Q3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a % 10 == b % 10:
    print("True")
else:
    print("False")
    
    
#Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.

for i in range(1, 11):
    print(i, end="\t")
    
    
#Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.


for i in range(23, 58):
    if i % 2 == 0:
        print(i)
        
#Q6. Write a program to check if a given number is prime or not.

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")


#Q7. Write a program to print prime numbers between 10 and 99.


for num in range(10, 100):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

#Q8. Write a program to print the sum of all the digits of a given number.


num = int(input("Enter a number: "))
sum_of_digits = 0

while num > 0:
    sum_of_digits += num % 10
    num = num // 10

print("Sum of digits:", sum_of_digits)


#Q9. Write a program to reverse a given number and print.


num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

print("Reversed number:", reversed_num)


#Q10. Write a program to find if the given number is palindrom or not.

num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

if original_num == reversed_num:
    print("Palindrome")
else:
    print("Not a palindrome")
    
    
    
    
    
    
                                       #Mini Project
                                       
                                       
#1.	create a python program that asks the user how far they want to travel. if they want to travel less than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. if they want to travel three hundred miles or more tell them to driver Super-Car.
#Sample Output:
#How far would you like to travel in miles? 2500
#I suggest Super-Car to your destination


distance = float(input("How far would you like to travel in miles? "))

if distance < 3:
    print("I suggest Bicycle to your destination")
elif distance < 300:
    print("I suggest Motor-cycle to your destination")
else:
    print("I suggest Super-Car to your destination")


#2.	Let's assume you are planning to use your python skills to build an App for Mobile.
#You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
#Write a python program that displays the answers to the following questions:
#How much does it cost to operate one server per day?
#How much does it cost to operate one server per week?
#How much does it cost to operate one server per month?
#How much days can I operate one server with $918?


hourly_rate = 0.51

# Calculations
cost_per_day = hourly_rate * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30
budget = 918
days_with_budget = budget / cost_per_day

# Display results
print("Cost to operate one server per day: $", round(cost_per_day, 2))
print("Cost to operate one server per week: $", round(cost_per_week, 2))
print("Cost to operate one server per month: $", round(cost_per_month, 2))
print("Number of days you can operate one server with $918:", round(days_with_budget, 2))
