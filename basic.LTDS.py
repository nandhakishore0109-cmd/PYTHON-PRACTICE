#LIST TO TUPLE CONVERSION ...

list = [1,23,354.76,"nandhakishoe","seetharampuram"]
list1 = tuple(list)
print(list)   #IT GENERATES LIST OUTPUT
print(list1)  #IT GENERATES AFTER TYPE CONVERSION


#TUPLE TO SET CONVERSION...

tuple = (23,"nandhunaidu",32.98,[1,"python",34,765.43],"pythonlife")
tuple1 = set(tuple)
print(tuple)    #IT IS OUTPUT FOR TUPLE
print(tuple1)  #IT IS OUTPUT FOR SET SFTER CONVERSION [IT SHOWS error BECAUSE SET DOES NOT CONTAIN LIST VALUES]

#SET TO LIST CONVERSION...

set = {1,234,"nandhu",(1,23,"kishore"),234,"nandhu",(1,23,"kishore")}
set1 = list(set)
set1.append("python")   #BY USING APPEND CHNAGES THE VALUES
print(set)  #IT IS OUTPUT FOR SET
print(set1)  #IT IS OUTPUT FOR LIST AFTER CHNAGING THE SET VALUES

# SET TO TUPLE CONVERSION...

Set2 = {123,143,"sathish",("sailesh",1234,86.45),143,123}
set3 = tuple(Set2)
print(Set2)  #SET OUTPUT
print(set3) #TUPLE OUTPUT

#TUPLE TO LIST CONVERSION..

my_tuple = (123,[1,234,"naidu"],23.76,"pushkar")
my_tuple1 = list(my_tuple)
my_tuple1.append("nandha")
print(my_tuple)    #TUPLE OUTPUT
print(my_tuple1)   #LIST OUTPUT WITH CHNAGES

#DICTIONARY DATA TYPE .....

my_dict = {"name":"nandhu","age":22,"city":"nellore","state":"AP"}
my_dict["pincode"] = 524310  #ADD NEW DICT
my_dict["age"] = 20        #UPDATE THE DICT(AGE)
my_dict.update({"name":"naidu","city":"vizag"})   #UPDATE MULTIPLE KEYS:VALUESS
print(my_dict)




#FIND THE LARGEST NUMBER....//By using comparison operators...
num1 = int(input("enter a value:"))
num2 = int(input("enter a value:"))
num3 = int(input("enter a value:"))
if (num1 > num2): 
   print(num1)
elif (num2 > num3): 
     print(num2)
elif (num1 > num3):
     print(num3)
else:              
     print(num3)