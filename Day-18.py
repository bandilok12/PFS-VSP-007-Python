'''
Usage of for with for...
Nested Loops --> Loops inside another loop.They are commonly used in pattern printing,matrix operations,
and solving various algorithm problems

Syntax:
for i in range(outer_loop_range):
    for j in range(inner_loop_range):
        #code..

#understand with a simple example
for i in range(3):  #outer loop runs 3 times
    for j in range(2):  #inner loop runs 2 times for each outer loop
        print(f'i={i},j={j}')
#for every outer loop inner loop will be completely executed...
#outer loop --> rows --> inner loop --> columns

for i in range(2):  #i --> 0,1
    for j in range(4):  #j --> 0,1,2,3
        print(i,j)
'''
#Number Patterns --> Row based number patterns,Column based number patterns...
'''
1 2 3
1 2 3
1 2 3

for i in range(1,4):
    for j in range(1,4):
        #print(i,j)
        print(j,end=" ")
    print()

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4

for i in range(1,5):
    for j in range(1,6):
        print(i,end=" ")
    print()

A A A A A
B B B B B
C C C C C

for i in range(1,4):
    for j in range(1,6):
        print(chr(64+i),end=" ")
    print()

A B C D
A B C D
A B C D
A B C D

for i in range(1,5):
    for j in range(1,5):
        print(chr(64+j),end=" ")
    print()

1 2 3
4 5 6
7 8 9

num =1
for i in range(1,4):
    for j in range(1,4):
        print(num,end=" ")
        num += 1
    print()

#Square Pattern --> * with n rows and columns
n = int(input("Enter the value:"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

#change this with different values --> Solid Rectangle
n = int(input("Enter the value:"))
for i in range(n):
    for j in range(n+1):
        print("*",end=" ")
    print()
'''
#Right angled Triangle
'''
*
* *
* * *
* * * *
* * * * *

n = int(input("Enter the value:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()

#Inverted Triangle
* * * * *
* * * *
* * *
* *
*

n = int(input("Enter the value:"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

1
2 3
4 5 6
7 8 9 10

num = 1
n = int(input("Enter the value:"))
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()

A
B C
D E F
G H I J

num = 1
n = int(input("Enter the value:"))
for i in range(1,n+1):
    for j in range(i):
        print(chr(64+num),end=" ")
        num+=1
    print()

A
A B
A B C
A B C D 
A B C D E

n = int(input("Enter the value:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
n = int(input("Enter the value:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
