'''
Built-in modules --> math,os,sys,platform,random,time,datetime...

#pip install <module>
import math     #it has all math constants,trignometric and basic math functions
#print(help(math)) #we can use help(obj) to get complete reference
print(math.ceil(2.1)) #returns the next higher value --> int
print(math.floor(2.8)) #returns the lowest value of given value --> int
print(math.e) #returns the exponential value
print(math.exp(2))
print(math.log(2))
print(math.log10(2))
print(math.pi)
print(math.factorial(8))
print(math.pow(3,6))
print(math.sqrt(6))
print(math.trunc(6.5))
print(math.modf(5.42))  #returns real and integral part

#os module --> os module provides functions to interact with the operating system
import os
#Current directory

print(os.getcwd())  #returns current working directory
print(os.listdir())     #returns the list of all files and folders in cwd..
for i in os.listdir():
    print(i)

#We can also create a folder and remove a folder
#print(os.mkdir("lokesh"))
print(os.removedirs("lokesh"))  #removes permanently
print(os.path.exists("lokesh"))  #checks for existence

#sys --> System specific parameters and functions
import sys
print(f'Python Version: {sys.version}')
print(sys.path)

#platform --> System and Platform Information
import platform
print(platform.system())    #returns OS name
print(platform.release())   #returns OS release version
print(platform.processor())     #returns processor type
'''
#random --> generating random numbers and choice
import random,time
#print(random.random())  #returns a value in interval of [0,1)
#to generate random integers
#print(random.randint(1,10)) #returns random integer in [a,b]
#OTP Generation
for i in range(10):
    print(random.randint(1000,9999))
    time.sleep(5)   #we can keep number of seconds as input
#lets get a word
user = input("Enter any --> Rock,Paper,Scissors").lower()
print(user)
system = random.choice(['rock','paper','scissors'])
print(system)
#Task --> Finish the Rock,Paper,Scissors Game
when = ['Last year','Long back','Once upon a time']
who = ['Devara','Rocky Bhai']
print(f'Here comes the story of {random.choice(who)} and is of {random.choice(when)}')
#Task --> Build a story generator
