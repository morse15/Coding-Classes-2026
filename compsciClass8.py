#9-6
#write an icecreamStand class that inherits from the restaurant class
from compsciClass7 import Restaurant
class icecreamStand(Restaurant):
    def __init__(self, Name,*flavors):
        super().__init__(Name,Cuisine = "")
        self.flavors = flavors
    #write a method that displays these flavours
    def displayFlavours(self):
        print (f"{list(self.flavors)}")
#add an attribute called "flavours" that stores a list of ice cream flavours

#test
IceCreamStand1 = icecreamStand("Cold Stone","Vanilla","Chocolate","Strawberry")
IceCreamStand1.displayFlavours()

#9-7
#use the User class
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

#write a class called admin that inherits from the user class
class Admin(User):
    #add attribute privileges that contains admin privileges
    def __init__(self, firstName, lastName, age, gender, loginAttempts=0,privileges = ["can add post","can delete post","can ban user"]):
        super().__init__(firstName, lastName, age, gender, loginAttempts)
        self.privileges = privileges
    #write method showPrivileges that prints privileges
    def showPrivileges(self):
        for privilege in self.privileges:
            print (privilege.title())

#create an instance of admin
admin1 = Admin("James","Smith",34,"M")
#call method
admin1.showPrivileges()