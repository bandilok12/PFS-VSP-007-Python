#Lists --> A list is an ordered,mutable,indexed and heterogeneous collection
#We use [] to represent lists
details = [1,'Lokesh','PFS7','Vizag',56.7]
print(len(details))
print(type(details))

stu_ids = ['CGVI0134','CGVI0135','CGVI0136']
print(stu_ids[1])
stu_ids[0]='Codegnan'
print(stu_ids)

#Tuples --> Tuples are also immutable,ordered,indexed and heterogenous collection
#We use parenthesis ()
#dimensions,coordinates
places = ('Viz','Hyd','Vij')
print(places)
print(len(places))
print(type(places))
places[0]='Chennai' #it is not possible as Tuples are immutable
print(places)

dimensions = 10,20,30 #By default Python considered it as tuple
print(dimensions)
print(type(dimensions))

#Sets --> A set is a unique collection(removes duplicates)
#A Set is an unordered,unindexed,mutable collection
ids = set()
print(ids)
ids = set((123,124,125,123))
print(ids)
courses = {'PFS','JFS','DA'}
print(courses)
print(type(courses))
print(courses[0]) #As Set is unordered there is no index

#Dictionaries --> A dictionary (mapping object) is a collection of key-value pairs --> dict = {k:v}
#We access only by keys (indexed by keys)
#Dictionary is also mutable collection
details = {'branch' : 'Vizag',
               'batches' : ['PFS-VSP-007','PFS-VSP-006'],
                'course' : 'PFS','count' : 19}
print(details)
print(type(details))
print(len(details))
print(details['batches'])

#Lists --> tuples,sets,dict,str,set
marks = [35,24,54]
a=tuple(marks)
print(a)
b=set(marks)
print(b)


#c=dict(marks)
e = dict.fromkeys(marks)
print(e)

#Tuple --> list,set,str,dict
marks = (35,24,54)
a = list(marks)
print(a)
b = set(marks)
print(b)
c = str(marks)
print(c)
d = dict(marks)
print(d)

#Dictionaries --> lists,tuples,sets
ids = {1:12,2:23}
print(list(ids))
print(tuple(ids))
print(set(ids))
print(str(ids))

#Frozensets --> It is an immutable set,unindexed,unordered
#We can typecase it to list, tuple, set
a = frozenset((12,32,12,32))
print(a)
print(type(a))
print(len(a))
b=list(a)
c=tuple(a)
d=set(a)
e=dict.fromkeys(a)
f=str(a)
print(c,d,e,f)
print(len(f))

a = 'lokesh'
e = list(a)
f = set(a)
g = tuple(a)
h = dict.fromkeys(a)
print(e,f,g,h)

#Operators --> Arithmetic,Assignment,Comparison,logical,Membership,Identity,Bitwise

#Arithmetic Operators --> +,-,*,**,/,//(floor division) quotient,%(modulus) remainder
a=3
b=2
print(a*b)
print(a**b)
print(a//b)
print(a%b)








