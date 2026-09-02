# TUPLESS....Immutable and similar to lists
# TASK-1 Create a Tuple Write a program that creates a tuple containing three 
#elements: your name, your age, and your favorite color.Then print the tuple
 
my_tuple = ('nandhu',29,'blue')
print(my_tuple)

# TASK-2 
# Write a program that creates a tuple containing the 
#days of the week. Then, print the third element of the tuple.

my_tuple = ('sunday','monday','tuesday','wednesday','thursday','friday','saturday')
print(my_tuple[2])

#TASK-3 
#Tuple Concatenation Write a program that creates two tuples, one 
#containing odd numbers from 1 to 5 and another containing even numbers 
#from 2 to 6. Concatenate these two tuples and print the result

tuple1 = (1,3,5,7)
tuple2 = (2,4,6,8)
print(tuple1 + tuple2)

# TASK-4
'''Tuple Unpacking Write a program that defines a tuple containing the 
dimensions of a rectangle (length and width). Then, unpack this tuple into 
two variables and calculate the area of the rectangle'''
length_rect = (12)
width_rect = (30)
result = length_rect * width_rect
print(f'The dimensions of rectangle is {result} ')

# TASK-5
'''Check if an Element Exists Write a program that checks if a given element 
exists in a tuple.'''
tuple = (1,2,'nandhu',99)
tuple_2 = (99 in tuple)
print(tuple_2)

# TASK-6 
'''Write a Python program to generate a bill for a supermarket purchase. The 
program should store the items and their prices in a list of tuples. It should 
then iterate over this list to print out each item along with its price. Finally, 
calculate and print the total cost of all the items
Sample Input:
items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
Sample Output:
Item
Price-------------------
Apple
99.00
Banana 99.00
Milk
49.00-------------------
Total
247.0'''

items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
total = 0
print('item'+" "*20+'price')
print("_"*55)
for i,j in items:
    print(i," "*20,float(j))
    total+= float(j)
print("_"*55)
print('Total'," "*25,total)