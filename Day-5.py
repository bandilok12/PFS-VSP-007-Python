#Operators --> Operators help us to perform operations between operands

#Arithmetic Operators -->+,-,*,/,**,//,%

#Assignment Operators --> It helps to assign,update(increment),decrement values
# = (assigning), += (Addition and assign), -= (Subtract and assign),*=,/=,//=,**=,%=

data=20
print(data)
print(type(data))

stock = data
print(stock)

#Increment the value of stock
stock = stock + 5 #stock+=5
print(stock)
print(data)

data=20
#Decrement the value of data by 2 values
data = data - 2
print(data)
stock-=data
print(stock)

data*=3
print(data)

data/=2
print(data)

data//=3
print(data)

data%=2
print(data)

stock = 100
stock**=2
print(stock)

#Comparison Operators (Relational Operators) --> It performs comparison
#between the operands and results in boolean True/False --> Conditions
# ==, !=, <,<=,>,>=

vinay_attendance = 75

print(vinay_attendance == 80)
print(vinay_attendance > 80)
print(vinay_attendance <= 80)
print(vinay_attendance < 80)
print(vinay_attendance >= 80)
print(vinay_attendance != 80)

#Logical Operators --> and,or,not (keywords)
#and --> it needs all conditions to be satisfied (two or more) --> True
#or --> it needs any one condition to be satisfied
#not --> opp to existing

max_marks = 70
pranay_marks = 75
max_att = 75
pranay_att = 70

pranay_marks +=20
certificate = pranay_marks >= max_marks and pranay_att >= max_att
print(certificate)
chance = pranay_marks >= max_marks or pranay_att >= max_att
print(chance)

data = []
print(data)
print(not(data)) #returns True
data = [1,2,3]
print(not(data))
#Both Logical and Comparison operators will return result in Boolean

#Membership Operators --> in,not in
#check for the existance in a sequence (str,list,set,tuple,dict)

names = ['vinay','vijay','raju']
name = 'ajay'
print(name in names)
print(name not in names)

print('25' in '325')
#print(12 in 121) #TypeError
print('arun' in 'arun')
print(['arun'] in ['arun'])

#Identity Operators --> It specifically refers to the object (memory location)
#id --> is,is not
a=14
b=14
print(a == b)
print(id(a))
print(id(b))
c=a
print(id(c))
print(c is a) #as id of both a and c are same -->True

a = [1,2,3]
b=[1,2,3]
print(a == b)
print(id(a))
print(id(b))
#as we have taken two lists eventhough with similar values identity
print(a is b)

c=a
print(id(c))
print(c is a)

a=(1,2,3,4)
b=(1,2,3,4)
print(id(a))
print(id(b))
print(a is b)

#When we check with the Interpreter mode and scripting mode above tuple result changes

#Bitwise Operators --> It performs bitwise operations --> &(Bitwise and), |(Bitwise or), ^(Bitwise XOR)
#An integer will be converted binary format and performs bitwise operation following integer to binary conversion

print(7&3)
print(7|3)
print(7^3) #XOR operation it returns 4
#7 to binary --> 0111
#3 to binary --> 0011
#7^3 --> 0100

#Shifting Operators(<< , >>)
print(7 << 1)
print(7 >> 1)













