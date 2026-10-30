'''
Tokens --> Operators --> Datatypes(Numeric,boolean,sequences -->str,lists,tuples,sets,frozensets,dicts)

Control Statements --> These are the statements which makes the programming flow to be possible.
They control the entire flow of the program
-->When to execute,what to execute,how to execute
-->Conditional statements -->if,elif,else
-->Jumping Statements -->break,continue,pass
assert,try,except,finally
-->Repetition Statements (Loops) -->for,while

#Conditional Statements -->Statements rely on the condition

Syntax if:

if <condition>:
    statement(s)
    ...

#data = False
data = True
if data:
    print("Welcome to Codegnan")
    print("This is PFS-VSP-007")
print("Guys are good but they will come late")

#mark = 25
mark = int(input("Enter a value:"))
marks = [12,14,16,25]
if mark in marks:
    print("Marks successfully fetched")
    print(f'Marks are {mark}')
print(f'It is done for the day')


stock = int(input("Enter the value:"))
total_stock = 100
if stock>0 and stock<total_stock:
    print(f'You can order the item')
    print(f'Item selected and placed into cart')
    print(f'Item ordered')

#Usage of else:

if <condition>:
    statement(s)...
else:
    statement(s)...

stock = int(input("Enter the value:"))
total_stock = 100
if stock>0 and stock<total_stock:
    print(f'You can order the item')
    print(f'Item selected and placed into cart')
    print(f'Item ordered')
else:
    print("Invalid Entry")

#Task: Vote Eligibility

Algorithm:
Accept the input from the user
Make the eligibility case as age greater than equal to 18:
    Eligibility granted
If age is not matching eligibility:
    Inform number of years to wait

Dry run:
Age --> 19 -->Result --> 19>=18 and 19>0
Age --> 12 -->Result --> 18-12 --> 6
Age --> -12 --> Result --> 18-(-12) --> 30

#Code
age = int(input("Enter your age:"))
if age>0:
    if age>=18:
        print("You are eligible to vote")
    else:
        print(f"You need to wait for {18-age} years")
else:
    print(f'Enter only positive values for the age')

#if-elif-else --> we wanted to map multiple conditions

if condition1:
    statement(s)..
    ...
elif condition2:
    statement(s)..
    ...
elif condition3:
    statement(s)..
    ...
else:
    statement(s)..
    ...
age = int(input("Enter your age:"))
if age>=18 and age<=100:
    print("You are eligible to vote")
elif age<0:
    print(f'Enter only positive values for the age')
elif age>100:
    print("Not eligible to vote")
else:
    print(f"You need to wait for {18-age} years")
'''
#Task --> Placement eligibility Tracker/System
print("---------PLACEMENT ELIGIBILITY CHECKER----------")
name = input("Enter the name of the Student:")
attendance = float(input("Enter the attendance of the student:"))
technical_score = float(input("Enter the Technical Score:"))
mock_interview_score = float(input("Enter the Mock Interview Score:"))
projects = int(input("Enter the number  of projects:"))

avg_score = (technical_score + mock_interview_score)/2
print("Student name is:",name)
if attendance >= 75 and avg_score >= 75 and projects > 2:
    print('Result: Student is Placement Ready he/she fails in Hotlist')
elif attendance >= 60 and avg_score >= 60 and projects > 1:
    print('Result: Student needs more preparation -->Improvement Stage')
else:
    print('Result: Student is in Foundation Stage-->Needs practice Session')






