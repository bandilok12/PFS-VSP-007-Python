name = "B.Venkata Sai Lokesh"
age = 22
place = "Visakhapatnam"
#Python is a case-sensitive eg:print(Age)
print(name)
#Snakecase convention(multiple words)
email_id = "sailokesh@gmail.com"
print(email_id)
branch_1 = "vijayawada"
print(branch_1)
true = 1

#Multiassignment of variables
name,email_id,mobile,gender = "Lokesh","sailokesh@gmail.com",9110590945,"Male"
print(name,mobile)
#Python by default follows Implicit type

name="Codegnan";age = 21;place="vizag"
print(name,age)

#Deletion --> del
del age,place #permanent deletion
print(age)

#Swapping of variables
a,b=15,25
print(a,b)
a,b=b,a     #value of a will become b
print(a,b)
c=a     #reassigning the existing value to a new variable
print(c)


#Literals
age=30
print(age)
taste = "bad"
print(taste)
price = 115.45
print(price)
print(type(price))
print(type(age))

#Identifiers --> names given to variables,functions,classes,objects,modules

#Punctuators ==> [ ] --> Lists, ( ) --> Tuples, { } --> Dictionaries,Sets

#Operators --> There are different type of operators
a=5
b=3
print(a/b)
print(a//b)
print(a%b)

#Raju purchased shoes with price 1000,discount 15%;how much raju has to pay?
price=1000
discount=0.15
final_price=price - (price*discount)
print(final_price)


#Vijay went to hotel for dinner his bill is 2500,GST applicable is 5%;hotel manager has given him 5% discount,how much Vijay has to pay?
