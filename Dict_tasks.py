# DICTIONARY TASKS USING PYTHON....

# TASK-1 Dictionary Update
'''Write Python code to add a new key-value pair to the following dictionary:
my_dict = {'name': 'python', 'age': 25}
# Output should be: {'name': 'python', 'age': 25, 'city': 'we
st godavari'}'''

my_dict = {'name': 'python','age':23}
my_dict['city'] = 'seetharampuram'
print(my_dict)

#Task 2: Dictionary Access
'''Write Python code to access and print the value associated with the key 'price' in 
the following dictionary:
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1
200}'''
# Output should be: 1200

my_dict = {'name':'laptop','brand':'dell','price':1200}
print(my_dict['price'])

# TASK-3 Dictionary Removal
'''Write Python code to remove the key-value pair with the key 'city' from the 
following dictionary:
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}'''
    # Output should be: {'name': 'John', 'age': 30}

my_dict = {'name':'nandhu','age':23,'city':'seetharampuram'}
my_dict.pop('city')
print(my_dict)    

# TASK-4 : Dictionary Keys
'''Write Python code to print all the keys present in the following dictionary:
# Your code here
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundr
y'}'''
# Output should be: ['name', 'age', 'city']

my_dict = {'name':'python','age':23,'city':'seetharampuram'}
print(my_dict.keys())

#Task 5: Dictionary Values
'''Write Python code to print all the values present in the following dictionary
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}'''
# Output should be: ['python', 25, 'tanuku']

my_dict = {'name':'python','age':23,'city':'seetharampuram'}
print(my_dict.values())
