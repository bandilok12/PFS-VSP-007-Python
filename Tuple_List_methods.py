
# Create a nested tuple containing lists
data = (
    [10, 20, 30],
    [40, 50],
    [1, 2, 2, 3, 4],
    [5, 3, 4, 1],
    ["apple", "banana", "cherry"],
    [100, 200, 300],
    ["Python", "Java"]
)
print(len(data))
print(data)

# 1. append()
data[0].append(40)
print(data[0])

# 2. extend()
data[1].extend([60, 70])
print(data[1])

# 3. insert()
data[2].insert(1, 99)
print(data[2])

# 4. remove()
data[2].remove(2)
print(data[2])

# 5. pop()
removed = data[2].pop(0)
print(data[2])
print(removed)

# 6. clear()
data[5].clear()
print(data[5])

# 7. index()
print(data[3].index(4))

# 8. count()
print(data[2].count(2))

# 9. sort()
data[3].sort()
print(data[3])

# 10. reverse()
data[3].reverse()
print(data[3])

# 11. copy()
copied_list = data[4].copy()
print(copied_list)
print(data)

print(data[4])
print(copied_list)
