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
'''
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
