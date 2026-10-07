Datatypes --> It will tell us how to define the data

#Python by default follows implicit type

#Numeric datatypes --> quantities,ids,stock,age --> int
age = 23
print(age)
print(type(age))

#float values --> salaries,price,percentage calculations --> float
salary = 15125.45
print(salary)
print(type(salary))

#complex --> real and imaginary values --> scientific calculations,signal processing
data = 3+5j
print(data)
print(type(data))

#Boolean --> True/False --> validations
access = True
print(type(access))

#None type --> None --> 0, False, ' ', [ ], ( ), { }, set() --> None cases in Python
branch_rank = None
print(type(branch_rank))
#Type Conversion --> converting one datatype to another datatype

#integer --> float,complex,boolean
#Every built-in datatype is a built-in function
rank=8
print(type(rank))

b=float(rank)
print(b)
print(type(b))

c=complex(rank)
print(c)

d=bool(rank) #bool(anything) is True, bool(nothing) is False
print(d)
print(type(d))

print(bool())
print(bool(0))
print(bool(None))
print(bool(''))
print(bool([]))
print(bool(['']))
print(bool([0]))
print(bool(' '))  #Space is also a character

#float --> integer, complex, boolean
temp=53.8
print(type(temp))
a=int(temp)
print(a)
b=complex(temp)
print(b)
c=bool(temp)
print(c)

#complex --> int, float, boolean
signal=5+6j

c=int(signal)
print(c)
d=float(signal)
print(d)

e=bool(signal)
print(e)

#boolean --> int,float,complex
access = True
print(int(access))
print(float(access))
print(complex(access))

a=int(float(bool(5)))
print(a)

b=bool(float(int(35)))
print(b)

c=True + 35 + 3.5 +(6+5j)
print(c)

#Sequence types --> strings, lists, sets, frozensets, dictionaries
#Strings --> group of characters
#quotations --> single, double, triple quotes
place="Codegnan"
print(type(place))
name="Lokesh"
print(name)
#Strings are immutable,ordered,indexed collection

print(len(name))
print(len(place))
print(len('qwerty'))

course = 'Python'
#print(int(course)) #ValueError
#print(float(course))
#print(complex(course))
print(bool(course))

#int, float, complex, bool ---> str
data=56
b=str(data) #it becomes numeric string
print(b)
mileage = 13.5
c=str(mileage)
print(type(c))
d = str(3+5j)
print(d)
e=str(True)
print(e)





