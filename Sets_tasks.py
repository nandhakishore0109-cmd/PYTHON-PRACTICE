# SETS TASKS...

#TASK-1 Set Intersection
'''Write Python code to find and print the intersection of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}'''
# Your code here
# Output should be: {4, 5}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result = set1.intersection(set2)
print(result)

# TASK-2 Set Union
'''Write Python code to find and print the union of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}'''
# Your code here
# Output should be: {1, 2, 3, 4, 5, 6, 7, 8}

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.union(set2))

# TASK-3  Set Difference
'''Write Python code to find and print the elements present in 
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}'''

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.difference(set2))

# TASK-4 Set Symmetric Difference
'''Write Python code to find and print the symmetric difference of the following 
two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}'''
# Output should be: {1, 2, 3, 6, 7, 8}
 
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.symmetric_difference(set2))

# TASK-5 Set Membership Test
'''Write Python code to check if the element 3 is present in the set 
my_set = {1, 2, 3, 4, 5}'''
# Output should be: True

set = {1,2,3,4,5,6}
if 7 in set:
    print(True)
else:
    print(False)    

'''Exercise 1: Set Intersection
my_set :
Write a Python script that finds and prints the intersection of two sets.'''

set1 = {'nandhu','vehana',2,3,5}
set2 = {2,3,4,6,7}
print(set1.intersection(set2))

'''Exercise 2: Set Union
Write a Python script that finds and prints the union of two sets.
'''

set1 = {'vehana','nandhu','sailesh',1,2}
set2 = {1,2,3,4,5}
print(set1.union(set2))

'''Exercise 3: Set Difference
Write a Python script that finds and prints the difference between two sets'''

set1 = {(1,2,3),'vehana','nandha',("vasu",'sailesh'),1,2}
set2 = {1,2,3,4,5,6}
print(set1.difference(set2))

'''Exercise 4: Set Symmetric Difference
Write a Python script that finds and prints the symmetric difference between 
two sets.
'''

set1 = {'vasu','nandhu','vehana',1,2,3}
set2 = {1,2,3,4,56,7}
print(set1.symmetric_difference(set2))

# DISJOINT SET.....
set1 = {(1,2,3),'nandu','vehana',2,8}
set2 = {1,2,3,45,6}
print(set1.isdisjoint(set2))

#SUPERSET & SUBSET...
set1 = {1,2,3,4,5}
set2 ={2,3,4,5,1}
print(set1.issuperset(set2))
print(set2.issubset(set2))


