#While ==> initalized statement ,counter..
#banking Scenario --> Pin authentication if more than
#3 attempts Account locked
pin = '2612'
max_attempts = 3
#You need to have a current attempt
current_attempt = 0
while current_attempt < max_attempts:
    enter_pin = input("Enter the ATM Pin:")
    if enter_pin == pin:
        print("Login Successful")
        print("Withdraw the Money...")
        break
        #continue --> it asks again to enter the pin 
    else:
        print("Entered pin is invalid.Try again carefully")
else:
    print("Account has been locked ..Try again after 24 hoours")

#BMI Scenario (usecase),We will makeuse of control Block Statments:
#BMI -->Body Mass index-->BMI = weight(kgs)/(height**2) (meters)
n = int(input("How many users"))
for i in range(n):
    weight = int(input("Enter the weight in Kgs:"))
    height = float(input("Enter the height in meters:"))
    name = input("Enter the name:")
    BMI = (weight)/((height)**2)
    if weight >0 and height>0:
        BMI = (weight)/((height)**2)
        #print(BMI)
        if BMI < 18.5:
            print(f"{name} -->You are underweight as BMI is {BMI}")
        elif BMI >=18.5 and BMI<=24.9:
            print(f'{name} -->You are in perfect physique ,BMI is {BMI}')
        elif BMI >= 25 and BMI <=29.9:
            print(f'{name} -->You are in over weight need to maintain diet ,BMI is {BMI}')
        elif BMI>=30:
            print(f"{name} -->Obesity, BMI is {BMI}")    
    else:
        print(f'Enter only +ve values')


#assert ---> It is mainly used in debugging checking during development
#it tests whether given condition is satisfied or not its
#a mandatory else it will raise the error.It is mainly used
# to catch bugs
#by ensuring the conditions hold True..
x = int(input("enter the value:"))
#assert x >0
assert x >0,"Enter the Positive value"
c =x**2
print(f'Final Result is {c}')
assert x in [24,25,12,10],"Checking Data"
print(f'Search Found') 

#Task :---> For same abovr BMI calculator , store the detials in dict


BMI_results = {
    'names': [],
    'BMI_values': []
}
n = int(input("How many users"))
for i in range(n):
    weight = int(input("Enter the weight in Kgs:"))
    height = float(input("Enter the height in meters:"))
    name = input("Enter the name:")
    if weight >0 and height>0:
        BMI = (weight)/((height)**2)
        BMI_results['names'].append(name)
        BMI_results['BMI_values'].append(round(BMI,3))
        #print(BMI)
        if BMI < 18.5:
            print(f"{name} -->You are underweight as BMI is {BMI:.3f}")
        elif BMI >=18.5 and BMI<=24.9:
            print(f'{name} -->You are in perfect physique ,BMI is {BMI:.3f}')
        elif BMI >= 25 and BMI <=29.9:
            print(f'{name} -->You are in over weight need to maintain diet ,BMI is {BMI:.3f}')
            
        elif BMI>=30:
            print(f"{name} -->Obesity, BMI is {BMI:.3f}")    
    else:
        print(f'Enter only +ve values')
print(BMI_results)
