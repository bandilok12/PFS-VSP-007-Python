'''
Functions --> A reusable block of code which performs a specific task

def fname(parameters):  #fun defn --> formal arguments
    """Doc string"""
    statement(s)......
    ........
    return value(s)...
fname(args)  #actual arguments

Types of arguments:
1. Positional Arguments --> count of arguments to be matched
2. Default Arguments --> we can make arguments as default
3. Keyword Arguments --> order/keyword name to be matched
4. Variable length arguments (*args) --> we can pass any number of positional arguments
5. Keyword variable length arguments (**kwargs) --> we can pass any number of keyword arguments

#Positional arguments --> count of arguments to be matched
def data(a,b,c):
    """Function to perform Arithmetic Operations"""
    d = a+b+c
    e = a-b-c
    f = a*b*c
    g = a/b/c
    return d,e,f,g
print(data(12,3,2))
#print(data(25,3,)) #TypeError as count is mismatched
#print(data(1,4,5,6,7)) #TypeError --> takes only 3 arguments
d,e,f = map(int,input().split())
result = data(d,e,f)
print(f'Result is {result}')

#Default arguments 
def data(a,b=5,c=4):    #non-default arguments always follows default arguments
    """Function to perform Arithmetic Operations"""
    d = a+b+c
    e = a-b-c
    f = a*b*c
    g = a/b/c
    return d,e,f,g
print(data(1,3,5))
print(data(24))     #here we need not mention other args as they are default
print(data(4,2))    #here one default argument taken
d = int(input())
print(data(d))      #mandatory count to be matched
#print(data(a=27,5,2))

#Keyword Arguments
#Grocery Purchase
#def grocery(item="Milk",price):    #Not at all possible
def grocery(item,price=40):
    """Usage of Keyword arguments"""
    print(f'Item is {item}')
    print(f'Value of item is {price}')
grocery("Pizza")
grocery("Milk",29)
#grocery(70,"Bread")    #in this case order differs result changes
print(grocery(price=45,item="Bread"))   #returns None
#grocery(items="Bottle",price=90) #TypeError --> keyword argument mismatch
'''
#Variable length arguments --> We can capture any number of positional
#arguments,we use (*args),captures excess positional arguments and
#pack them into tuple...

def sample(*a):
    """Usage of arbitrary arguments"""
    print(a)
    print(type(a))
sample()
sample(1,2)
sample('saketh','codegnan')
sample([12,3,4,5])
