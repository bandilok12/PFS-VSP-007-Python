'''
#Best Seller Tag Display
product_sale = int(input("Enter the sales:"))
if product_sale > 1000:
    print("Best Seller")
else:
    print("No Output")

raining = bool(input())
print(raining)
print(type(raining))
if raining:
    print("Extra Rain Charges Applied")
else:
    print("No Output")

#Delivery Charge Calculation
order_value = int(input("Enter order amount:"))
if order_value <=99:
    print(f"Final Bill Amount:{order_value+30}")
else:
    print(f"Final Bill Amount:{order_value}")

#Budget Plan
budget = int(input("Enter the budget:"))
if budget > 10000:
    print("Plan: Trip")
elif budget > 5000:
    print("Plan: Resort Stay")
elif budget > 3000:
    print("Plan: Movie and Dinner")
elif budget > 1000:
    print("Plan: Cafe and Shopping")
elif budget > 500:
    print("Plan: Street Food and Park Visit")
else:
    print("Plan: Stay Home")
'''

#Repetition Statements (Loops) --> Loops helps us in automating repetitive tasks --> for,while
#Usage of for: -->It is used mainly to iterate within in lists,strings,ranges..
'''
Syntax:
for <temp> in collection/range:
    statement(s)...
    ....

#marks = [25,20,21,19,10,12]
#Marks can be dynamic
marks = list(map(int,input("Enter the marks:").split(',')))
print(marks)
for i in marks:
    print(i)    #it traverses within the loop

#Cal the total marks
marks = list(map(int,input("Enter the marks:").split(',')))
total = 0
for mark in marks:
    #print(i)    #it traverses within the loop
    #we need to update total with each mark
    total = total + mark    #total += mark
    print(total)
print(f'Total marks are:{total}')
print(f'Average marks are :{total/len(marks)}')

subject = input("Enter the subject:")
for i in subject:
    print(i)

details = {'ids':[121,123,125],
           'marks':[25,20,21]}
for data in details:    #indexed through keys
    print(data)
    
for data in details.values():
    print(data)

for key,value in details.items():
    print(key,value)

for data in details:
    print(details[data])    #it returns values

#range(stop) --> takes by default minimum value as 0
for i in range(5):
    print(f'Value of i is {i}')
    print(f'Square of i is {i**2}')

#range(start,stop) --> u can mention start and stop positions(values)
#start is included,end is excluded
for i in range(1,11):
    print(i,i**2)
    print('<------->')

#range(start,stop,step)
for i in range(1,21,1):
    print(i)

for i in range(1,21,2):
    print(i)

#Get first 10 even numbers
for i in range(2,21,2):
    print(i)
#print numbers from 10 to 1 in reverse order
for i in range(10,0,-1):
    print(i)
#print 'A' to 'Z' in a single line
for i in range(65,91):
    print(chr(i),end=' ')

names = ['Akash','Kaushik','Vijay','Sanjay','Lokesh']
for name in names:
    print(name,end=' ') #this returns horizontal order

for i in range(len(names)):
    print(names[i])

#Ask input from user and get the sum of numbers as per input
n = int(input("Enter a value:"))
if n<0:
    print("No Output")
else:
    total=0
    for i in range(1,n+1):
        total += i
    print(total)
'''

#Usecase : Checking daily workout app usage
work_log = [1,1,1,0,1,1,0]
#1 --> workout done
#0 --> workout missing
#Find the longest workout streak
longest_streak=0
current_streak=0
for day in work_log:
    if day == 1:
        current_streak += 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0
print(f'Longest Streak is {longest_streak}')
