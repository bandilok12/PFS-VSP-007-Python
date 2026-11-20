'''
reduce()---> It Reduces an iterable into a single value...
It repeatedly applies a function to combine elements....
we can use it from functools
syntax ---> reduce(function,iterable)

from functools import reduce

#Sum of numbers from a iterable
numbers = [1,5,2,3,4]
result = reduce(lambda a,b:a+b,numbers)
print(result)

#Largest number from a collection
data = list(map(int,input().split()))
print(data)
result = reduce(lambda a,b:a if a>b else b,data)
print(result)

#Return the longest word in a group of strings
words = ['Python','Developer','SQL','Programming']
longest = reduce(lambda a,b : a if len(a) > len(b) else b,words)
print(longest)

#map() --> transformations
#filter() --> selection
#reduce() --> aggregation

#List comprehensions --> In Python,it is a precise way to create lists
#Syntax --> [expression for item in iterable]
#iterable --> list,set,dict or range()
li = []
for i in range(10):
    #print(i)
    li.append(i)
print(li)
#or
li = [i for i in range(10)]
print(li)

#Squares of 1-10 numbers in a list
squares = [i**2 for i in range(1,11)]
print(squares)

#Even numbers in a list
even = [i for i in range(1,11) if i%2==0]
print(even)

#Update scores of each person with 10 marks
scores = [25,45,50,60,55]
f_scores = [i+10 for i in scores]
print(f_scores)
#or
m_scores = list(map(lambda i:i+10,scores))
print(m_scores)

names = ['saketh','codegnan','vizag']
#result = ['SAKETH','CODEGNAN','VIZAG']
result = [i.upper() for i in names]
print(result)
#or
result = list(map(lambda i:i.upper(),names))
print(result)

#List Comprehension with if-else usage
#[true_value if condition else false_value for item in iterable]
data = [12,4,5,6,8,9]
print(data)
result_1 = ["Even" if i%2==0 else "Odd" for i in data]
print(result_1)
result_2 = [i**2 if i%2==0 else i**3 for i in data]
print(result_2)

#nested List comprehensions --> One inside another
#[expression for i in iterable1 for j in iterable2]

colors = ['Red','Blue','White']
sizes = ['S','M','L','XL']
dress = [(color,size) for color in colors for size in sizes]
print(dress)

d = [(i,j) for i in range(1,5) for j in range(1,5)]
print(d)
print(*d)

#Multiplication table pattern
data = [[i*j for i in range(1,11)] for j in range(1,11)]
#print(data)

print(*data)
#get the table pattern in vertical order

#Nested comprehension with if condition
#Syntax:[expression for i in iterable1 for j in iterable2 if condition]
#possible pairs without matching values
data = [(i,j) for i in range(1,4) for j in range(1,4) if i!=j]
print(data)

f = [i*j for i in range(1,4) for j in range(1,4) if i!=j]
print(f)
print(*f)

#nested comprehension with if-else usage
#[true_value if condition else false_value]
#for item1 in iterable1 for item2 in iterable2]

week1 = [15,20,25,22,18,19]
week2 = [23,19,25,18,19,25]

result = ["Improved" if x<y else "Lagged" for x in week1 for y in week2]
print(result)
#make sure to check the braces and closures
#In the above case if we replace [] braces with () --> we do not get tuple

#Generators
result = ("Improved" if x<y else "Lagged" for x in week1 for y in week2)
print(result)
'''
#Generator --> It is a special function,which produces one value at a time
#we use yield keyword
'''
def fname():
    """doc string"""
    return value(s)...
    ...
fname()

def fname():
    """doc string"""
    yield value1
    yield value2
    yield value3
    ....
fname()

def func():
    """Normal Function"""
    return [1,2,3,4,5]
    #return "lokesh"    A function can have return with multiple values
#print(func())
data = func()
for i in data:
    print(i)

def func():
    """Generator Function"""
    yield 1
    yield 2
    yield 3
b = func()
print(next(b))
print(next(b))
print(next(b))
#print(next(b)) Stops the iteration

def display():
    """Subjects Covered"""
    yield ["Python",45,"Paper Based Exams"]
    yield ["Aptitude",65,'Weekly Exams']
    yield ["Softskills",60,"Activities"]
    yield ["Frontend",45,"Projects"]
    yield ["FastAPI",45,'Integration']
print(display())
g = display()
print(f'Subject allotted is {next(g)}')
print(f'Subject allotted is {next(g)}')
print(f'Subject allotted is {next(g)}')

week_1 = [20,14]
week_2 = [15,18]
result = ("Improved" if x<y else "Lagged" for x in week_1 for y in week_2)
#print(result)
g = result
print(next(g))
print(next(g)) #next() function will fetch the value from generator
print(*result)
'''
#Exception Handling --> It is the mechanism in Python to respond to runtime errors or exceptions
#Exception is an event that occurs during the execution of a program which disrupts its normal flow 
#TypeError,ValueError,IndexError,AttributeError,KeyError,ZeroDivisionError

#We will be using try,except and finally..
'''
Syntax:
try:  #you write code which may cause an error
    #code that raise an exception
except ExceptionType:   #it handles the error if it occurs
    #code to handle the exception
'''
#Basic Exception Handling
a,b = 5,0
try:
    result = a/b
    print(f'Answer is {result}')
except Exception as e:
    print(f'Error is {e}')
