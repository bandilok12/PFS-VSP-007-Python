'''
Functions are termed as First Class Objects.
Anonymous Functions : An anonymous function is a nameless function with lambda keyword to use it.

They are generally used for short simple, operations can be written in a single line,
they are also termed as Lambda Functions.
They are generally used with filter(),map() and reduce()

Syntax :
lambda argument(s) : expression

#Create a function to get the area of triangle
def rectangle(l,b):
    """Area of Rectangle"""
    return l*b
print(rectangle(7,5))

area = lambda l,b : l*b
print(f'Area of Rectangle is {area(7,5)}')

#Square of a number
def square(number):
    """Square of a number"""
    return number**2
number = int(input())
print(f'Square of a {number} is {square(number)}')

number = int(input())
square = lambda number : number ** 2
print(f'Square of a {number} is {square(number)}')

#Find Maximum of two numbers
def maximum(a,b):
    """Maximum of two numbers"""
    return a if a>b else b
print(maximum(10,35))

maximum = lambda a,b : a if a>b else b
print(maximum(10,35))

#No Parameters
greet = lambda : "Welcome to Vizag"
print(greet())

#filter() used to select elements from an iterable based on a condition
#Only the elements that satisfy the condition are returned 

#filter(function,iterable)

numbers = [1,2,4,6,7,8,9,10,12,45,67]

#Even numbers --> [2,4,6,8,10,12]
#Normal function
def even(numbers):
    """Even Numbers from list"""
    even_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
    return even_list
print(even(numbers))

even_result = list(filter(lambda num : num%2==0,numbers))
print(even_result)
odd_result = list(filter(lambda num : num%2!=0,numbers))
print(odd_result)

prices = [500,650,1200,800,900]
#Products above 700
result = list(filter(lambda price:price>700,prices))
print(result)

#map() applies transformation to every element in a collection
#map(function,*iterables)

scores = [15,20,19,23]
result = list(map(lambda new_score:new_score+1,scores))
print(result)

d = list(map(int,input().split()))   #list of integers
print(d)

#Add GST --> 18%
prices = [1000,2000,3000]
final_price = list(map(lambda price:price+(price*0.18),prices))
print(final_price)
'''
#Calculate length of objects in a collection
subjects = ['Python','SQL','Aptitude','Softskills']
result = list(map(lambda word:len(word),subjects))
print(result)







