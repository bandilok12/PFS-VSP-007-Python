'''
Sequences --> Strings,Lists [],Tuples (),Sets set(),Dictionaries {}
Lists [] --> A list is an ordered,mutable,indexed and heterogeneous collection
It will be dynamic in size
'''
#Creation of Lists
details = [123,"Saketh",32,"PFS",75.5]
print(type(details))
print(len(details))
print(details)

#Nested Lists
batches = [["PFS","PFS-VSP-007","PFS-VSP-008"],
                ["DA","DA-VSP-007","DA-VSP-008"],
                   "Vizag",8]
print(len(batches))
print(type(batches))
              
#Indexing,Slicing,Striding
print(batches[0])
print(batches[-3])
print(batches[1:4])
print(batches[:2])
print(batches[1:5:2])
print(batches[-5:-1:4])
print(batches[-1:-5])

#Subindexing --> Accessing index within the index of a collection(str,list,tuple)
print(batches[0])
print(batches[0][1])
print(type(batches[0][1]))
print(batches[0][1][4:7])
print(batches[0][1][4:7][::2])
print(batches[2])
print(batches[2][2:])

#Lists supports repetition,merging and its also an iterable (iterate through loops)
print(batches[0][1][:3] + batches[0][1][-4:])
print(batches[1][2])
print(batches[1][2][-3:])

print([1,2,3]*3) #Repetition
# print([1,2,3]+3) #TypeError
print([1,2,3] + batches) #Merging

print('Vizag' in batches)   #Membership
print('PFS' in batches)
print('PFS' in batches[0])

#Lists methods
data = []
#print(dir(data))    #returns list of all available methods
#append(), extend(), insert()

#append(obj) --> insert object to the end of the list
data.append(24)
print(data)
data.append('Vizag')
print(data)
#data.append('Python','MYSQL') #TypeError
data.append(['Python','MYSQL'])
print(data)
print(len(data))

#extend(obj) --> insert multiple elements (objects) to the end of the list
data.extend(['Python','MYSQL'])
print(data)
data.extend('vizag')
print(data)

#insert(index,object) --> inserts elements before index
data.insert(2,'lokesh')
print(data)
data.insert(-3,'codegnan')
print(data)
data.insert(2,[34,12,54])
print(data)

#Lists are mutable
marks = [25,24,27,28,30,35,36]
print(marks)
marks[2] = 45
print(marks)
marks[:3] = ['lokesh','codegnan']
print(marks)
#In above cases data is being modified in original list
#Indexing case length remains constant but data is modified where as in slicing case it may increase,decrease

#pop(), remove(), clear() --> removes elements from the list
subjects = ['Python','Aptitude','SS','MYSQL','Flask']

#pop() --> removes by default last element if index is not mentioned
print(subjects.pop()) 
print(subjects.pop(2))
#print(subjects.pop(5)) #raises IndexError
print(subjects)

#remove() --> removes specific value from the collection
subjects.remove('Python')
#print(subjects.remove('Python'))   #returns None
#subjects.remove("Codegnan") #ValueError

#clear() --> removes all elements from the list and returns empty list
subjects.clear()
print(subjects)

#index(),count()
#index(start)   #returns only first occurrance index position
marks = [24,25,24,26,27,30]
print(marks.index(24))
print(marks.index(24,1))
#print(marks.index(545))    #ValueError

#count() --> returns the count of occurrances
print(marks.count(24))
print(marks.count(248))

#Task:Create a nested List with lists and strings and perform list methods
