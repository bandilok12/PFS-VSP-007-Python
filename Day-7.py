'''
Sequences --> Strings,Lists,Tuples,Sets,FrozenSets,Dicts

Strings --> A string is a group of characters.It is immutable,ordered,indexed collection.
We can denote it in single,double or triple quotes
'''
data = '' #empty string
print(type(data))
print(len(data))

#Operations --> Concatenation,Repetition,Indexed,Slicing
#Concatenation --> combining multiple strings
sub1 = "Python"
sub2 = "MYSQL"
print(sub1+sub2)
print(sub1+","+sub2)
print(sub1+" <-> "+sub2)

#Repetition --> String can be repeated any number of items with a valid int
print("*")
print("*" * 10)
name = "Lokesh";place = "Vizag"
print(f'{name * 5}')
print(f'---->{name} is in ---->{place}')

#Membership --> in,not in
print("jay" in "Ajay") #returns True
print("Jay" in "Ajay")  #returns False

#Indexing --> Accessing each position(index) in an object
#It starts at 0 and ends at len(obj) - 1
s="I am from Vizag"
print(len(s))
#Traversing the elements --> Positive Indexing  
print(s[8])
#print(s[17]) #IndexError
#Negative Indexing --> starts from back it is denoted as -1 to -len(obj)
print(s[-1])
print(s[-4])

#Slicing --> group of characters --> [start:end] start is included, end is excluded (len(obj) -1)
s="Codegnan"
print(s[:])
print(s[2:])
print(s[0:4])
print(s[4:8])
print(s[:4])
print(s[3:20])
print(s[24:]) #returns empty string
print(s[5:1])   #returns empty string as positive slicing lower index to higher index

print(s[-1:])   #returns only last character
print(s[-5:-1]) #same including negative indices with same symbols lower to higher index
print(s[:-5])
print(s[:-6] + s[-6:])

print(s[1:-1])
print(s[-1:3])  #returns empty string

#Task -->create a string and explore above possibilities

#Striding --> [start:end:step] --> Now we can specifically get desired character in an interval
#print(s[::0])  #returns ValueError
print(s[::1])
print(s[::2])
print(s[::3])

place = "Visakhapatnam"
print(place[:4])
print(place[-6:])
print(place[1:7:2])
print(place[-5:-1:3])

#what if we give -1 in interval
print(place[::-1])  #This helps to return in reverse order
print(place[::-2]) #this skips one element in reverse order

#You can explore all cases in Striding
print(place[1:7:-2])

#Built-in functions --> type(),len(),min(),max(),ord(),chr(),sorted()
password = "admin123"
print(len(password))
print(type(password))
print(min(password))    #min() returns min object in collection
#ASCII values follows
print(ord('A'))
print(ord('a'))
print(ord('z'))
print(chr(120))
print(sorted(password))












