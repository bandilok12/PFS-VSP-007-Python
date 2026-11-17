'''
Built-in Functions --> Functions which are built-in in Python
abs(),any(),all(),bin(),bool().....

dir(__builtins__) --> enumerate(),zip()

details = ['Codegnan','Saketh','PFS-VSP-007']

0 : Codegnan
1 : Saketh
2 : PFS-VSP-007

for i in details:
    print(details.index(i),':',i) 
for i in range(len(details)):
    print(i,':',details[i])

for i,z in enumerate(details):
    print(f'{i} : {z}')

#enumerate() will create a counter object for an iterable
#zip() will combine multiple iterables into a single iterable

data = ['Ajay','Sai','Sanjay']
marks = (20,25,24)
#place = ('Vizag','Vjwda','Hyd')
details = dict(zip(data,marks)) #if we take one more iterable it raises ValueError
print(details)

emails = input().split()
print(emails)
for email in emails:
    print(email.split('@')[1])

orders = list(map(int,input().split()))
print(orders)

#eval() --> You can take any input --> dict
salaries = eval(input("Enter the salaries:"))
print(salaries)
print(type(salaries))

print(int(4.56))
#round() --> it will round off to next decimals
print(round(4.56))  
print(round(4.567,2))
'''
#Function is termed as First class Object
#Recursive Functions --> A function calling itself where it makes the smaller problem
#is broken into multiple times...
#depends on two cases --> Base case (it indicates when to stop recursion)
                                    #--> Recursive case (it makes the problem to be repeated)
'''
Syntax:
def function():
    if base_condition:
        return
    function()  #we write our recursive 
function()

#Factorial Approach using Recursion
def factorial(x):
    if x == 0 or x == 1:
        return 1
    elif x<0:
        return "No negative values only positive numbers to be accepted"
    else:
        return x*factorial(x-1)
n = int(input("Enter a value:"))
print(factorial(n))

#Sum of Natural numbers using recursive logic
def sum_of_natural(x):
    if x == 0 or x == 1:
        return 1
    elif x<0:
        return "No negative values only positive numbers to be accepted"
    else:
        return x+sum_of_natural(x-1)
n = int(input("Enter a value:"))
print(sum_of_natural(n))

Task:Build a Simple Choice Chooser:
----------------WELCOME TO GAME--------------------
1 --> Recursion logic Factorial
2 --> Sum of Natural numbers(recursion)
3 --> BMI Calculation
4 --> Fibonacci Series
5 --> ATM usecase
any other number --> only enter 1-5
Q --> Quit
'''
