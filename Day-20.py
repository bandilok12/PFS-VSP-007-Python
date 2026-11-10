'''
Python --> POP, OOP
POP --> Procedure Oriented Programming --> Functions

Function --> A function is a block of code (statements) which performs a specific task.
It is a reusable code --> readability,reusability and easy to maintain

Types of Functions:
1. User Defined Function --> def
2. Built-in Functions --> Python by default(print,len,min,max,sorted,str,list,bool,dict,...)
3. Anonymous Functions --> Nameless Functions --> lambda (map,filter) reduce
4. Recursive Functions --> Recursion --> Factorial,Fibonacci --> Decorators

Syntax:

def fname(parameters): #Function header
    """Doc String (Description of function)"""
    statement(s).......   #Body of function
    .................
    return value(s)
fname(args) #function call
'''
#Simple Function to understand the reusability
'''
a = 20
b = 10
print(a+b)

def add(a,b):
    """This function returns the sum of given objects"""
    c = a+b
    #print(c)
    return c

print(add(24,25))
add(16.5,23.4)
print(add('code','gnan'))
print(add([1,5],[2,3,4]))
add((1,2),(5,6))

def add(a,b):
    """Sample Add function"""
    return f'Result is {a+b}'
c,d = map(int,input().split())
print(add(c,d))
print(add("code","gnan"))
g,h = 54,-23.5
e = add(g,h) #Assigning function to a variable
print(e)
'''
#Functions are also objects

def greeting():
    """Greetings to the User"""
    #return "Hey guys Welcome to Codegnan"
    #return 24+34 #A function can have multiple values to return but not multiple return statements
    return "Hey guys","Python","PFS-VSP-007"
    #return len(("Hey guys","Python","PFS-VSP-007"))
#print(greeting())
print(greeting() * 5)
print(type(greeting))   #returns Function
print(type(greeting()))     #returns type of Function
