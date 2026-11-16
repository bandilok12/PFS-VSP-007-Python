#Pass by Reference --> When mutable objects (Lists,Sets,dict) are passed into the function
#changes inside the function affect the original object...
'''
def update(items):
    """We will assume items as list"""
    #items.append("Laptop")
    items.extend(["Laptop","Power Bank","Camera"])
cart = ["Mobile","Watch"]
print(update(cart)) #returns None
print(cart) #original list changes
#print(update("lokesh"))  #raises AttributeError

#Dictionary Usage --> Updating profile
def update(profile):
    """Usage of Dictionary"""
    profile['branch'] = "Vizag"
students = {'names':['Sanjay','Akash']}
pfs_students = {'batches':['PFS-VSP-007','PFS-VSP-006'],
                'subjects':['Python','MYSQL','Aptitude']}
update(students)
print(students)
update(pfs_students)
print(pfs_students)

#Pass by value --> Original data will not change,immutable objects
#Pass by object reference --> Original data will change,mutable objects

#Built-in functions --> Functions which are inbuilt in Python
#print(),len(),min(),max(),sorted(),int(),float(),bool(),complex(),str(),list(),
#tuple(),set(),dict(),input(),eval(),help(),sum()

#print(dir())
#print(dir(__builtins__))    #returns list of all errors and functions 
#print(help(print))
#print(help(len))

#abs(),chr(),ord()
print(abs(-34)) #returns the absolute value of numbers
print(chr(68))
print(ord('@')) #returns the ASCII value
data = [24,56,78,0]
print(any(data)) #any() --> compares bool(x) for any value --> True
print(all(data))    #all() --> needs all values to be present
#print(all(None))
print(all([None]))
print(bin(6)) #returns binary object

#enumerate()
print(help(enumerate))

data = ["Akash","Ajay","Sanjay"]
c = dict(enumerate(data))   #by default it creates a counter object
print(c)

d = dict(enumerate(data,1))
print(d)
''' 
#zip() --> it combines multiple collections into a single collection
data = ["Sanjay","Akash","Vijay","Ajay","Bharath"]
marks = [25,20,23,21,18]
f = dict(zip(data,marks)) #zip checks for length matching
print(f)
