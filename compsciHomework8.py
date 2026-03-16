#9-8
#write a seperate privileges class using what you did in 9-7
class Privileges:
    def __init__(self,privileges):
        self.privileges = privileges
        self.privileges = ["can add post","can delete post","can ban user"]
    def showPrivileges(self):
        for privilege in self.privileges:
            print (privilege.title())

#9-9
#use electricCar.py as given in the question
class Car:
    #A simple attempt to represent a car.
    def __init__(self, make, model, year):
    #Initialize attributes to describe a car.
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
#Return a neatly formatted descriptive name.
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
    #Print a statement showing the car's mileage.
        print(f"This car has {self.odometer_reading} miles on it.")

class Battery:
#A simple attempt to model a battery for an electric car.
    def __init__(self, battery_size=40):
#Initialize the battery's attributes.
        self.battery_size = battery_size
    def describe_battery(self):
        #Print a statement describing the battery size.
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
    #Print a statement about the range this battery provides.
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
    #Q - make a method called upgradeBattery that sets the battery size to 65 if it is not already
    def upgradeBattery(self):
        if self.battery_size != 65:
            self.battery_size = 65
        else:
            print("This battery is at the expected size.")

class ElectricCar(Car):
    #Represent aspects of a car, specific to electric vehicles.
    def __init__(self, make, model, year):
#Initialize attributes of the parent class.
#Then initialize attributes specific to an electric car.
        super().__init__(make, model, year)
        self.battery = Battery()
#Q - make an instance of electricCar
car = ElectricCar("Tesla","Cybertruck","2022")
#call get_range
car.battery.get_range()
#upgrade battery
car.battery.upgradeBattery()
#call get_range again
car.battery.get_range()

#9-13
#make a class "Die" with attribute 'sides'
from random import randint
class Die:
    #sides should default to 6
    def __init__(self,sides = 6):
        self.sides = sides
    #write method rollDie which simulates rolling a die
    def rollDie(self):
        number = randint(1,self.sides)
        print (f"\n This die has {self.sides} sides")
        print (f"The rolled number is {number}")
#create an instance of die
dice1 = Die()
#roll dice1 10 times
dice1.rollDie()
dice1.rollDie()
dice1.rollDie()
dice1.rollDie()
dice1.rollDie()
dice1.rollDie()
dice1.rollDie()
dice1.rollDie()
dice1.rollDie()
dice1.rollDie()

#make a 10 sided die
dice2 = Die(10)
#rollDie 10 times
dice2.rollDie()
dice2.rollDie()
dice2.rollDie()
dice2.rollDie()
dice2.rollDie()
dice2.rollDie()
dice2.rollDie()
dice2.rollDie()
dice2.rollDie()
dice2.rollDie()

#make a 20 sided die
dice3 = Die(20)
#rollDie 10 times
dice3.rollDie()
dice3.rollDie()
dice3.rollDie()
dice3.rollDie()
dice3.rollDie()
dice3.rollDie()
dice3.rollDie()
dice3.rollDie()
dice3.rollDie()
dice3.rollDie()

#9-14
#make a list containing 10 numbers and 5 letters
list1 = ["a",1,"b",2,"c",3,"d",4,"e",5,"f","g","h","i","j"]
from random import choice

w = choice(list1)
i = choice(list1)
nn = choice(list1)
er = choice(list1)
winner = f"{choice(list1)}{choice(list1)}{choice(list1)}{choice(list1)}"
winner = list(winner)
print(winner)
print (f"\nThe winning ticket is {w},{i},{nn},{er}")

#9-15
#write a list called my ticket
#write a loop that only stops once your ticket has won and print how many loops it took to get there
myTicket = ["a",1,"b",2]
counter = 0
# while True:
#     w1 = choice(list1)
#     i1 = choice(list1)
#     nn1 = choice(list1)
#     er1 = choice(list1)
#     if [w1,i1,nn1,er1] == myTicket:
#         print("Your ticket has won!")
#         counter = counter + 1
#         print(f"It took {counter} tries for your ticket to win")
#         break
#     else:
#         print("Better luck next time")
#         counter = counter + 1
#         print(f"This is try {counter}")
        
