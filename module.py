'''
Modules --> User Defined Modules --> Create,Accessing.
Built-in Modules --> math,os,sys,etc
A module is a Python file(.py) consists of objects,variables,function
we use import keyword..

import Day_31
print(dir(Day_31)) #use dir to get list of all available methods and attributes
print(type(Day_31.greet))
print(Day_31.greet("Lokesh"))
print(type(Day_31.names))
print(Day_31.names.items())

print(Day_31.__doc__) #returns docstring (description of module)
print(__doc__)  #returns current file docstring

Day_31.names.update({"Place":"Vizag","subjects":['Python','Aptitude','SQL']})

print(Day_31.names)
print(len(Day_31.names))

#Accessing methods or attributes using from keyword
from Day_31 import greet
print(greet("Codegnan"))

#print(names) #this is not possible as we didn't import it
from Day_31 import greet,names  #we can import multiple attributes
print(names)

#Aliasing module names
import Day_31 as d
print(d.greet("Vijay"))
print(d.names.keys())
'''
#To access all methods or attributes we use '*' 
from Day_31 import *  #this is only recommend for user/simple modules
print(names)
print(greet("Saketh"))
f = display()
print(next(f))


