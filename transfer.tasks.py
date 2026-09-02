# TRANSFER STATEMENTS TASKS

# TASK-1  Using break in a While Loop
'''Write a Python program that takes a list of numbers as input 
numbers = [25, 30, 
20, 40, 15, 25] and prints the sum of the numbers. However, if the sum exceeds 
100, stop adding numbers and print "Sum exceeded 100"'''

numbers = [25, 30, 20, 40, 15, 25] 
sum = 0 
for i in numbers:
    sum+= i
    if sum>=100:
        break
print(sum) # SUM THE INPUT AND BREAKS WHEN INPOT REACHES 100
print(i)   # PRINT LAST ITERATION 

# TASK-2 Using continue in a For Loop
'''Write a Python script that uses a for loop to iterate through numbers from 1 to 
600. Print only the odd numbers, skipping the even ones using the 
statement.'''

for i in range(1,600):
    if i%2==0:
        continue
    print(i)
print(f"The last iteration is {i}")

# TASK-3  Using pass in Conditional Statements
"""Write a Python script that checks if a number is even or odd. If the number is 
even, print "Even"; if odd, do nothing (use the 
pass statement"""

num = int(input("enter a num :"))
if num%2==0:
    print("even")
else:
    pass   

# TASK-4 Combining Transfer Statements
'''Write a Python script that iterates through a list of words. If the word is "break," 
exit the loop using the 
break statement. If the word is "skip," skip the rest of the 
code for the current iteration using the 
continue statement. For any other word, 
print the word.'''

my_list = ['nandhu','vehana','sonu','skip','vamsi','krishna','break','rayudu','mani']
for i in my_list:
    if i == 'skip':
        continue
    elif i == 'break':
        break
    print(i)


