# PYTHON_STRINGS TASKS 

# TASK-1 You are given a string 
'''Example:
sentence . Print the characters at even indices.
sentence = "Python is amazing"
# Output: "Pto saaig'''

str = "python is amazing"
result = ""
for i in range(0,len(str),2):
    result = result +str[i]
print(f'"{result}"')

# TASK-2 Problem:
'''You are given a string 
s . Replace all spaces in the string with underscores (
and print the modified string.
Example:
s = "Python is fun and powerful"
# Output: "Python_is_fun_and_powerful"'''

str = "Python is fun and powerful"
result = str.replace(" ","_")
print(result)

# TASK-3 You are given a string 
'''Example:
s = "12345"
s . Check if the string contains only digits'''

str = "123456"
result = str.isdigit()
print(result)

# TASK-4 You are given a string 
'''Example:
 . Print the string in reverse order.
s = "Python is amazing"
# Output: "gnizama si nohtyP"'''

str = "Python is amazing"
print(str[::-1])

# TASK-5 You are given a string 
'''  Capitalize the first letter of each word in the string 
and print the modified string.
Example:
s = "python programming is fun"
# Output: "Python Programming Is Fun"'''

str = "Python programming is fun"
str1 = str.split()
for i in range(len(str1)):
    str1[i] = str1[i].capitalize()
    result = " ".join(str1)
print(result)    

