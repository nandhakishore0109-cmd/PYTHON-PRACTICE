# CONDITIONAL STATEMENTS....(if, if-else, if-elif-else, nested if-else, short if-else )
#  TASKS DAY 5 ....(conditional statements)

 # TASK-1  Vowel Checker:
'''Write a Python program that takes a character as input and checks whether 
it is a vowel or not. Use the 
if-else statement.'''

char = input("enter a char:")
result = "aeiouAEIOU"
if char in result:
    print(f"yes ur char in vowels list {result}")
else:
    print("not in vowels")  

# TASK-2  Age Group Classification
'''Write a program that takes an age as input and classifies the person into 
one of the following age groups:
Child: 012 years
Teenager: 1317 years
Adult: 1864 years
Senior: 65 years and older'''

age = float(input("enter a age:"))
if age>=100 or age<=0:
    print(" enter valid age")
elif age >= 65:
    print("senior citizen")
elif age >= 18:
    print("adult citizen")
elif age >= 13:
    print("teenager")
else:
    print("child")   


# TASK-3 Number Classifier:
'''Write a program that takes an integer as input and classifies it as positive, 
negative, or zero. Use the 
if-elif-else statement. '''

num = int(input("enter a value"))
if num>0:
    print(f"Given num is +ve {num}")
elif num<0:
    print(f"Given num is -ve {num}")
else:
    print(f"Given num is zero")

# TASK-4   Leap Year Checker:
'''Create a program that checks whether a given year is a leap year or not. A 
leap year is divisible by 4, but not by 100 unless it is divisible by 4'''

year = int(input("enter a year:"))
if year%4==0:
    print(f"Given year is leap year {year}")
else:
    print(f"Given year is not leap {year}")    

# TASK-5  Calculator:
'''Build a simple calculator program that takes two numbers and an operator 
(+, -, *, /) as input and performs the corresponding operation'''

num1 = int(input("enter a value:"))
num2 = int(input("enter a value:"))
operator = input("enter operator('+','-', '*', '/'):")
if operator == '+':
   print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print("invalid operator")    

# TASK-6  Short Hand If:
'''Rewrite the following code using the short-hand 
if statement:
2
Quiz Questions:
x = 8
if x % 2 == 0: result = "Even"
else: result = "Odd"'''

num = int(input("enter a value:"))
print(f"even") if num%2 == 0  else print("odd")

# TASK-7 Discount Calculator:
'''Create a program that calculates the final price after applying a discount. 
The program should take the original price and the discount percentage as 
input.'''

org_price = float(input("enter a price:"))
discount = int(input("enter a discount value:"))
result = org_price * (discount/100)
org_price += result
print(result)
print(org_price)

# TASK-8 BMI Calculator:
'''Write a program that calculates the Body Mass Index BMI using the 
formula: BMI  weight (kg) / (height (m))^2. The program should take 
weight and height as input'''

weight = float(input("enter a value (kg):"))
height = float(input("enter a height (m):"))
BMI = (weight / (height ** 2))             # FORMULA
print(f"The  body mass index is {BMI} ")



             


