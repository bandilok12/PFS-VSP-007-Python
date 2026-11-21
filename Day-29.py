'''
#Basic Exception Handling
a,b = 5,0
try:
    result = a/b
    print(f'Answer is {result}')
except Exception as e:
    print(f'Error is {e}')

#a,b = map(int,input("Enter the values:").split())
#print(a,b)
try:
    a,b = map(int,input("Enter the values:").split())
    print(a,b)
    result = a/b
    print(f'Answer is {result}')
except Exception as e:
    print(f'Error is {e}')

#Multiple Except Blocks
try:
    a,b = map(int,input("Enter the values:").split())
    #print(a,b)
    result = a/b
    print(f'Answer is {result}')
except ValueError:
    print("Values should be only 2 and only integers")
except ZeroDivisionError:
    print("Cannot divide by zero")
except NameError:
    print("Name is not defined")

try:
    subjects = ['Python',45,'AI',50]
    #print(subjects[5])
    subjects.append("SQL")
    print(subjects)
except Exception as e:  #this can be written if you want exception to take care
    print(e)
except IndexError:
    print("Make sure to check the length of the list")
except NameError:
    print("Check the spelling")
except AttributeError:
    print("Check the method properly")
finally:
    print("Anyways this will be printed")

#Catching Multiple Exceptions Together
try:
    value = int(input("Enter a value:"))
    #result = 10/vlue check this case
    f = 10/value
    print(f)
except (ValueError,ZeroDivisionError,NameError) as e:
    print(f'An Error occurred:{e}')
'''
#Raising Exceptions
#You can raise exceptions intentionally using raise keyword
'''
value = 15
if value < 0:
    raise ValueError("Value cannot be negative")
#else:
#    print("Done")

Custom Error Messages:
try:
    raise Exception("Custom Error Message")
except Exception as e:
    print(e)

try:
    value = -15
    if value < 0 or value in [1,20]:
        raise Exception("Value is negative")
except Exception as e:
    print(e)

def fn(a,b):
    """testing"""
    return a*b
print(fn(50,20))

File Handling --> open()

File and directory operations are essential to store the data..
Python provides build-in function --> open()

#mode of operations --> 'r','w','r+','w+'
#open(filename,mode) #default mode is 'r'
try:
    file = open('new.txt',"r")
    print(file)
    #print(file.read())  #reads the entire content
    #print(file.readline())  #reads a single line
    print(file.readlines()) #read all lines into a list
except Exception as e:
    print(e)
'''

    
