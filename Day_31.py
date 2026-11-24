'''
Modules --> User Defined Modules --> Create,Accessing.
A module is a Python file(.py) consists of objects,variables,function
we use import keyword..
'''
def greet(name):
    """User defined function"""
    return f'Hello {name}! Welcome to Codegnan'
#print(greet("Lokesh"))

names = {'Students':['Vinay','Deepak','Lokesh'],
         'age':[25,22,24]}
print(__name__)

def display():
    """Generator Function"""
    yield "Python"
    yield "Aptitude"

#if __name__ == "__main__":
#    print(greet("Lokesh"))
#    names['batch']='PFS-VSP-007'
#    print(names)
