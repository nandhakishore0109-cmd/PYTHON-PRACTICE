#ARTHEMETIC OPERATORS....

num1 = 30
num2 = 20
print(num1 + num2)  #ADDITIONAL OPERATOR
print(num1 - num2)  #SUB OPERATOR
print(num1 * num2)  #MULTIPLE OPERATOR
print(num1 / num2)  #DIV OPERATOR
print(num1 % num2)  #MODULOR DIVISION 
print(num1 // num2)  #FLOOR DIVISION
print(num1**num2)   #EXPONENTION OPERATOR


"""(A+B)**2 PROGRAM"""

a = int(input("enter a value:"))
b = int(input("enter a value:"))
result = (a+b)**2  #FORMULA
print(result)

#ASSIGNMENT OPERATORS....

nandhu = 100
nandhu+=1  #INCREMENT
nandhu-=10 #DECREMENT
nandhu*=1
print(nandhu)

#COMPARISION OPERATORS...

num1 = 1000
num2 = 1500
print(num1>num2)  #GRATER THAN
print(num1==num2)  #EQUAL TO
print(num1!=num2)  #NOT EQUALS TO


#LOGICAL OPERATORS...

person_age = 19
education = "b.tech"
print(person_age >= 18 and education == "b.tech" ) #PERFORMS AND OPERATION


premium = True
discount = 3000
print(premium  or dicount <= 5000)  # OR OPERATOR

# MEMBERSHIP OPERATORS
courses = ['sql','c++','python','java','c','html']
print('sql' in courses)
print('python' not in courses)  # IN & NOT IN OPERATORS


#CALCULATE AREA OF RECTANGLE...
length = int(input("enter a value:"))
width =  int(input("enter a value:"))
breadth = ("enter a value:")
result = length * width        #FORMULA OF AREA OF RECTANGLE
print(f"The area of rectangle is {result}")  # By using F-strings we print reasonable output


#CONVERT GIVEN TEMP CELSIUS TO FAHRENHITS....
given_temp = int(input("enter a value:"))
fah = (given_temp * (9/5)) + 32  #Formula for cel to fah conversion...
print(f"The given_temp is {given_temp} after conversion final fahrenhit is {fah}") #By using F-strings


 #STRING CONCATINATION...... 
str1 = input("enter a str:")
str2 = input("enter a str:")
str_concat = str1 + str2   #By using '+' operation we concat two strings into single word or line....
print(f"The string concatination is {str_concat}") 


# PROGRAM TO CALCULATE SIMPLE INTEREST...
principal = 20000
interest = 2
time = 3
simple_interest = (principal * interest * time) / 100  # Formula for simple_interest 
principal += simple_interest  # Total amount simple_interst + principle
print(simple_interest)        #How much interst after 3 years
print("Total amount", principal) # Total

# AVERAGE OF 3 NUMBERS.....
num1 = int(input())
num2 = int(input())
num3 = int(input())
avg = (num1 + num2 + num3)/3  # FORMULA 
print(avg)

# CONVERT KM TO METERS USING ARTHEMETIC.....
kilometer = int(input())
meters = kilometer * 1000
print(f"The given kilometers is {kilometer} after convert into meters then final meters is {meters}")