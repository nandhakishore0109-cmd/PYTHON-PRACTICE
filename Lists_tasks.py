# LISTS METHODS TASKS....

# TASK-1 Reverse List:
'''Write Python code to reverse the order of elements in the given list 
Print the reversed list.
my_list = [10, 20, 30, 40, 50, 11]
# Your code here
my_list . 
# Output should be: [11,50,40,30,20,10'''

my_list = [10,20,30,40,50,11]
print(my_list[::-1])

# TASK-2 Common Elements:
'''Given two lists 
them.
list1 and 
list2 , find and print the common elements between 
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]'''

list1 = [1,2,3,4,5,]
list2 = [4,5,6,7,8]
empty_list =[]
for i in list1:
    for j in list2:
        if i == j:
            empty_list.append(i)
print(empty_list)    

# TASK-3 Unique Elements:
'''Create a new list 
unique_list containing only the unique elements from the 
given list 
original_list . Print the unique list.
original_list = [1, 2, 2, 3, 4, 4, 5]
# Your code here
# Output should be: [1, 2, 3, 4, 5]'''

my_list = [1,2,2,3,3,4,4,5]
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)   

# TASK-4 Remove Duplicates:
'''Remove duplicate elements from the given list 
without duplicates while preserving the order.
duplicated_list and print the list 
duplicated_list = [1, 2, 2, 3, 4, 4, 5]'''
# Your code here
# Output should be: [1, 2, 3, 4, 5]

my_list = [1,2,2,3,4,3,5]
new_list= []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)     


'''Exercise 1 List Concatenation
Write a Python script that concatenates two lists and prints the result.'''

list1 = [1,2,3,4,5]
list2 = ['nandhu','vamsi','vehana','jamesh','sailesh']
print(list1+list2)
'''Exercise 2 List Repetition
Write a Python script that repeats a list three times and prints the result.'''

my_list = [1,'vehana',2,'nandhu',3,'sailesh']
print(my_list*3)

'''Exercise 3 List Removal
Write a Python script that removes the elements at even indices from a list.'''

my_list = [1,2,3,4,5,6]
print(my_list[::2])

#Exercise 4 List Insertion
'''Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list'''
my_list = [1,2,3,17,76,87]
my_list.insert(0,10)
my_list.insert(1,11)
my_list.insert(2,12)
print(my_list)

#List comprehensions
''' Square Numbers Create a list of squares of numbers from 1 to 10.'''


new_list = []
for i in range(1,10):
    n=i**2
    new_list.append(n)
print(new_list)   

result = [i**2 for i in range(1,10)]
print(result)


''' Even Numbers Generate a list of even numbers from 1 to 20.'''

result = [i for i in range(1,20) if i%2==0]
print(result)

'''Words Lengths Given a list of words, create a list containing the lengths of 
each word.'''
'''words = ["apple", "banana", "cherry", "date"]'''

words = ["apple", "banana", "cherry", "date"]
result = [len(i) for i in words]
print(result)

