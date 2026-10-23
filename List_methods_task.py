#Task:Create a Nested List with lists and strings and perform List methods

college = [
    ["CSE", "ECE"],
    ["CSE-101","CSE-103"],
    "Hyderabad",
    2026,
    ["Python","SQL"]
]

print(len(college))     #Output:5
print(type(college))    #Output:<class 'list'>

# append()
college.append("Computer Science")
print(college)
'''
Output:
[['CSE', 'ECE'], ['CSE-101', 'CSE-103'],
'Hyderabad', 2026, ['Python', 'SQL'], 'Computer Science']
'''
# extend()
college.extend(["Library", "Laboratory"])
print(college)
'''
Output:
[['CSE', 'ECE'], ['CSE-101', 'CSE-103'], 'Hyderabad', 2026,
['Python', 'SQL'],'Computer Science', 'Library', 'Laboratory']
'''
# insert()
college.insert(2, "Main Campus")
print(college)
'''
Output:
[['CSE', 'ECE'], ['CSE-101', 'CSE-103'], 'Main Campus', 'Hyderabad', 2026,
['Python', 'SQL'], 'Computer Science', 'Library', 'Laboratory']
'''
# pop()
print(college.pop(3))#Hyderabad
print(college)
'''
Output:
[['CSE', 'ECE'], ['CSE-101', 'CSE-103'], 'Main Campus', 2026,
['Python', 'SQL'], 'Computer Science', 'Library', 'Laboratory']
'''
# remove()
college.remove("Laboratory")
print(college)
'''
Output:
[['CSE', 'ECE'], ['CSE-101', 'CSE-103'], 'Main Campus',
2026, ['Python', 'SQL'], 'Computer Science', 'Library']
'''
# count()
college.extend(["Library", "Library"])
print(college.count("Library"))     #Output:3

# index()
print(college.index("Library"))     #Output:6

# clear()
temp = ["HTML", "CSS", "JavaScript"]
temp.clear()
print(temp)     #Output:[]
