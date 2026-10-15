
Tokens,datatypes(Numeric,boolean,none type,sequences(str,lists,tuples,sets,
frozensets mapping objects(dicts)) typecasting
operators
input Formatting/output Formatting


#Input foramting --->input()
#Usage of input()
#we can pass any type of object as input --->result is in only sring
name=input("enter the name:")
print(name)
print(type(name))

#integer input-->int()
roll_number=int(input("enter the roll number:"))
print(roll_number)
print(type(roll_number))

#Float Input -->float()
marks =float(input("enter the marks:"))
print(marks)
print(type(marks))

#Group of strings (group of values as strings)
#return List
#group of the strings(mutiple vlues as strings)
names=input().split()# we need default values
names=input("enter the subjects:").split(',')
print(names)
print(type(names))
#comma separated value name
name,batch=input("enter the details:").split()
print(name)
print(batch)

#multiple integer values
#we will use map()
order_id,cost=map(float,input().split())
print(order_id,cost)

subjects,marks=map(float,input().split())

py_marks,ap_marks,ss_marks,sql_marks=map(float,input().split())
print(py_marks,ap_marks,ss_marks,sql_marks)
#Group of integer float values

stu_marks=list(map(int,input().split(',')))
print(stu_marks)

discounts=list(map(float,input("enter the discount:").split(',')))
print(discounts)

#Accept the cost of selling the product from user and also the original cost
#of the product and determine the profit/loss amount for the user

original_amount=float(input())
selling_amount=float(input())
profit=original_amount-selling_amount
print(profit)

#set of integers
#set of Float values--->replace in with float
ids=set(map(int,input("enter ids").split(',')))
print(ids)
print(type(ids))

#passing dict data using eval

stu_details=eval(input("enter the data:"))
print(stu_details)

#So using eval() u can pass any type of data

#Output Formatting --> print()
a,b,c = map(str,input("Enter the names:").split())
print(a,b,c)
#now we will use sep --> sep is the keyword
print(a,b,c,sep="----")
#end is specifically telling how u wanna end the statements
print(a,b,c,sep=":",end="\t")   #here end = tab space character
print("Saketh","Vizag",end=" ") #here end = space character
print(34,4.5)

#1) Using commas in print()
name = "Codegnan";branch = "Vizag";batch = 'PFS-VSP-007'
print(name,"is in",branch)
print(batch,"belongs to",branch,"branch")

#2) Using %(modulus) formatting -->old style C Programming
#%d -->integers,%f -->float,%s -->strings
age = 32
price = 45.256
place = "Vizag"
print("Age = %d | Price = %f | Place = %s"%(age,price,place))
print("Price is %.f"%price) #in this case complete decimal part is wiped off
print("Price is %.2f"%price) #rounding off to two decimals

#3) Usage of String formatting --> str.format()
name = "Codegnan";branch = "Vizag";age = 8
print("{} is in {} and its of {} years in Edtech Industry".format(name,branch,age))

a,b = 2,45
print("{1},{0}".format(a,b))
print("Value of a is {} and value of b is {}".format(a,b))

#f-string notation --> Python 3.9+ versions
print(f"{name} is in {branch}")
#make sure to denote the variables only in curly braces
print(f'Value of a is {a} and b is {b}')
print(f'"Codegnan is in {branch} and of {age} years in Trainings"')












