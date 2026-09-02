# ADVANCED FUNCTIONS(lamda(),map(),filter(),reduce())

'''Write a Python function 
square_all(numbers) that takes a list of numbers as input 
and returns a new list containing the square of each number in the input list. 
Use the 
map() function with a lambda function to implement this'''

list1 = [1,2,3,4,5]
result = map(lambda x : x**2,list1)
print( list(result))


'''Write a Python function 
filter_positive(numbers) that takes a list of numbers as 
input and returns a new list containing only the positive numbers from the 
input list. Use the 
filter() function with a lambda function to implement this.'''

list2 = [1,-1,0,3,-2,-4,3]
def positive(list2):
    return filter(lambda x:x>0,list2)  
print(list(positive(list2)))

'''Write a Python function 
calculate_factorial(n) that calculates the factorial of a 
given number n. Use the 
reduce() function with an appropriate lambda 
function to implement this.'''

from functools import reduce
def factorial(n):
    fact = reduce(lambda x,y:x*y , range(1,n+1))
    return fact
print(factorial(5))

'''Write a Python function 
count_vowels(string) that takes a string as input and 
returns the count of vowels (a, e, i, o, u) in the input string. Use the 
reduce() 
function with an appropriate lambda function to implement this'''

from functools import reduce
def vowels(string):
    vowels = {'a','e','i','o','u','A','E','U','O','I'}
    result = reduce(lambda count,char:count+(1 if char in vowels else 0) , string,0 )
print((vowels("HI Im here")))    