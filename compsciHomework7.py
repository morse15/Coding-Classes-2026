#8-16
#import a program you wrote
import moduleTest
moduleTest.printed("Hello World")

from moduleTest import printed
moduleTest.printed("Hello World")

from moduleTest import printed as pr
pr("Hello World")

import moduleTest as mT
mT.printed("Hello World")

from moduleTest import *
moduleTest.printed("Hello World")

#9-2
#use code from 9-1
class Restaurant:
    def __init__(self,name,cuisine,numberServed = 0):
        self.name = name
        self.cuisine = cuisine
        self.numServed = numberServed
    def describe(self):
        print(f"{self.name} is a {self.cuisine} restaurant and has served {self.numServed} customers")
    def open(self):
        print(f"{self.name} is open")
    def set_numberServed(self,numberServed):
        self.numServed = numberServed
    def increment_numberServed(self,numberServed):
        self.numServed += numberServed

#create three instances of restaurant
Restaurant1 = Restaurant("McDonalds","American")
Restaurant2 = Restaurant("Sky Garden","English")
Restaurant3 = Restaurant("Mega Chicken","Nigerian")
#describe all instances
Restaurant1.describe()
Restaurant2.describe()
Restaurant3.describe()

#9-3
#make a class called user, having first name, last name, e.t.c
class User:
    def __init__(self,firstName,lastName,age,gender,loginAttempts=0):
        self.firstN = firstName
        self.lastN = lastName
        self.age = age
        self.gender = gender
        self.loginAttempts = loginAttempts
    #make a method called describeUser which describes the user
    def describeUser(self):
        print(f"\nFirst Name: {self.firstN} \nSurname: {self.lastN} \nAge: {self.age} \nGender: {self.gender}\n")
    def greetUser(self):
        print(f"Welcome {self.firstN} {self.lastN}\n")
    def increment_loginAttempts(self):
        self.loginAttempts = self.loginAttempts+1
        print(f"{self.loginAttempts}")
    def reset_loginAttempts(self):
        self.loginAttempts = 0
        print(f"{self.loginAttempts}")

person = User("John","Smith",43,"M")
person1 = User("Jill","Jackson",31,"F")
person2 = User("Hello","World",10,"")
#describe and greet all instances
person.describeUser()
person.greetUser()
person1.describeUser()
person1.greetUser()
person2.describeUser()
person2.greetUser()

#9-4
#add an attribute called numberServed with a default of 0 to the code from 9-1
#make a new instance and print numberServed default and the changed
Restaurant4 = Restaurant("Blah","Italian")
Restaurant4.describe()
Restaurant5 = Restaurant("Bleh","French",3000)
Restaurant5.describe()
#add a method that lets you set the number of customers that have been served
Restaurant5.set_numberServed(30)
Restaurant5.describe()
#add a method that lets you increment the number of customers served then call it
Restaurant5.increment_numberServed(15)
Restaurant5.describe()

#9-5
#add attribute loginAttempts to user class
#write method increment_loginAttempts which increments loginAttempts by 1
#write method reset_loginAttempts which resets loginAttempts to 0
person3 = User("Jane","Doe",30,"F")
#call increment multiple times and verify that it works
person3.increment_loginAttempts()
person3.increment_loginAttempts()
person3.increment_loginAttempts()
person3.increment_loginAttempts()
#call reset and verify it works
person3.reset_loginAttempts()