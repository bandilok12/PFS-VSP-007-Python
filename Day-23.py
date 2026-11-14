'''
#Usage of Variable length and Keyword Variable length arguments

def scores(*marks,branch = "Codegnan",**names):
    """Scores Scenario with Variable and keyword variable length args"""
    print(marks)
    print(names)
    total = 0
    for mark in marks:
        if type(mark) in (int,float):
            total += mark
    print(f'Total marks are: {total}')
    for name,value in names.items():
    #for name in names.values():
        print(f'Name: {name}')
        print(f'Value: {value}')
    print(f'Branch is {branch}')
scores(25,20,15,18,16,name="Ajay",place="Vizag",batch="PFS-VSP-007")
#Positional arguments always follows keyword arguments
#Non-default always follows default arguments
'''
#Scope --> Determines where a variable can be accessed within a program
#A variable is only accessible within the region where it is defined
'''
Types of Scope:Local Scope,Global Scope,Global Keyword,Nonlocal Scope

#Local Scope:Variables defined and accessible only inside the function...

def fname():
    """Usage of local variables"""
    name = "Codegnan"
    return f'{name} is in Vizag'
print(fname())
#print(name)    #NameError as LocalScope name is inside the function
print(fname())
name = "Lokesh"
print(name)

#Global Variable --> A variable declared outside all functions is called a global variable.
#It can be accessed from anywhere in the program.
name = "Codegnan"
def uname():
    """Global Scope"""
    return f'{name} is in Vizag,Vijayawada, and Hyderabad'
print(uname())
print(name)

#Local variables get higher priority inside the function
name = "Codegnan"
def uname():
    """Global Scope"""
    name = "Saketh"
    return f'{name} is in Vizag,Vijayawada, and Hyderabad'
print(uname())
print(name)

#Global keyword --> Used when we want to modify a global variable inside the function
count = 15
def update():
    """Global Keyword usage"""
    global count
    count += 5  #UnboundLocalError so we need to use global keyword
    return f'Updated count is {count}'
print(update())
values = [1,3,45]
values.append(count)
print(values)

#NonLocal Scope --> Used in Nested Functions..Allows modifications of
#variables from the outer function

def outer():
    """Outer Function"""
    count = 10
    def inner():
        """Inner Function"""
        nonlocal count
        count = count + 15
        return f'Result from Inner function is {count}'
    print(inner())
    return f'Result from outer function is {count}'
print(outer())

#LEGB ==> Local --> Enclosing --> Global --> Built-in

len = 45
a = ['codegnan','python']
#print(len(a))   #Here we have used built-in function as identifier it fails

#Functions are termed as First class Objects
#Pass by Value and Pass by Object Reference

#Pass by Value --> Immutable objects
#int,float,bool,str,tuple,complex,frozenset
#When immutable objects are passed to function,changes inside the function
#do not effect the original value

def update(number):
    """Pass by value usage"""
    number = 15
    print("Inside function:",number)
number =32
update(number)
print("Outside Function:",number)
'''
def update(number):
    """Pass by value usage"""
    return number*3
    #print("Inside function:",number)
number =32
print(update(number))
print(update(25))
