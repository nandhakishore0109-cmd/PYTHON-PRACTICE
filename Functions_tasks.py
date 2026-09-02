# FUNCTION TASKS.....

# Task 1: Add Function
'''Write a Python function named 
returns their sum.'''

def add(a,b):
    print(a+b)
add(10,22)    

# SQUARE FUNCTION:
'''Write a Python function named 
square that takes a number 
x as input and 
returns its square.'''

def square(a):
    result = a**2
    print(result)
square(4) 

# TASK-3 FACTORIAL NUMBER
"""Write a Python function named 
input and returns its factorial.
factorial that takes a positive integer""" 

import math
def factorial(x):
    result = math.factorial(x)
    print(result)
factorial(5)    


#Task 4: Maximum Function
'''Write a Python function named 
maximum that takes a list of numbers as input and 
returns the maximum value in the list'''

def maximum(x):
    max_value = max(x)
    print(max_value)
maximum([10, 23, 65, 76, 00, 34, 100])  


# TASK-5 REVERSE FUNCTION
'''Write a Python function named 
reverse that takes a string 
returns its reverse.'''

def reverse(*s):
    reverse_str = s[::-1]
    print(reverse_str)
reverse('nandhu','nani','vehana','sailesh','sumith')    

# PRIME FUNCTION
'''write a Python function named 
is_prime that takes a positive integer 
n as input 
and returns 
True if 
n is prime, otherwise 
false'''


def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print('not prime')
                break

        else:
            print('prime')
    else:
        print('Given input is not prime')            
prime(27)

# Fibonacci Function
'''Write a Python function named 
input and returns the 
fibonacci that takes a positive integer 
n as 
n th Fibonacci number'''

def fibonacci(a):
    if a>1:
        num = (a-1)+(a-2)
        print(num)
    else:
        print('Given num is wrong')
fibonacci(45)

#Task 8: Palindrome Function
'''Write a Python function named 
is_palindrome that takes a string 
returns 
True if 
s is a palindrome, otherwise false'''

def palindrome(n):
    if n==(n[::-1]):
      print("palindrome")
    else:
        print("not palindrome")
palindrome("121")          

# TASK-9 Sum of Squares Function
'''Write a Python function named.
sum_of_squares that takes a list of numbers as 
input and returns the sum of the squares of those numbers.'''
                
def sum_of_squares(n):
    sum = 0
    for i in range(1,n+1):
        sum+= i**2
        print(f"sum of squares {sum}")
    else:
       print("not found")
sum_of_squares(6)            

#Write a Python function named average that takes a list of numbers as input and returns the average value.

def average(n):
    avg = 0 
    for i in range(1,n+1):
        avg+=(i)/n
    print(f'Average value is {avg}')
average(10)        


    
