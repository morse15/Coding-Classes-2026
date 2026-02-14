#7-1
#ask the user what type of car they want to rent
rentalCar = input("What kind of rental car would you like? : ")
#print a message containing the user response
print(f"Let me see if I can find you a {rentalCar.strip()}...")
print("\n")

#7-2
#ask user how many people in their dinner group
dinnerGroup = int(input("How many people are in your dinner group: "))
#if the answer>8 tell them they have to wait for a table, else tell them a table is ready
if dinnerGroup > 8:
    print ("You will have to wait for a table...")
else: 
    print ("Your table is ready.")
print("\n")

#7-3
#ask user for a number
num = int(input("Please input a number: "))
#check if the number is a multiple of 10 and tell the user
if num % 10 == 0:
    print ("This number is a multiple of 10")
else:
    print ("This number is not a multiple of 10")
print ("\n")

#7-4
#let the user add pizza toppings until they 'quit'
pizzaToppings  = []
toppings = ""
print ("Please enter your required toppings one by one")
print ("When you are done type 'quit' in the terminal")
while toppings != ("quit"):
    toppings = input("Topping: ")
    toppings = toppings.lower()
    toppings = toppings.strip()
    if toppings != ("quit"):
        print(f"We'll add {toppings}")
        pizzaToppings.append(toppings)
    else:
        print ("quitting...")
print("\n")
print ("Your pizza topping are below:")
for pizzaTopping in pizzaToppings:
    print (pizzaTopping)
print("\n")

#7-5
#write a loop that asks age and outputs the price of tickets
customers = int(input("How many people are you trying to buy tickets for: "))
for customer in range(customers):
    age = int(input(f"What is the age of person {(customer)+1}: "))
    if age<3:
        print ("This ticket is free")
        print ("\n")
    elif age<13:
        print ("This ticket costs $10")
        print ("\n")
    else:
        print ("This ticket costs $15")
        print("\n")
print("\n")

#7-6
#rewrite 7-5 to stop when the user inputs 'quit'
print ("Please type the age of the person who is going to use the ticket when prompted with 'Age: ' ")
print ("If you wish to exit the loop, type 'yes' when prompted, otherwise type 'no'. ")
quit = ("no")
while quit == ("no"):
    age = int((input("Age: ")))
    if age<3:
        print ("This ticket is free")
        print ("\n")
    elif age<13:
        print ("This ticket costs $10")
        print ("\n")
    else:
        print ("This ticket costs $15")
        print("\n")
    quit1 = input("Do you wish to quit: ")
    quit1 = quit1.strip()
    quit1 = quit1.lower()
    quit = quit1
print ("\n")

#7-7 
#run a loop that never ends
while True:
    print ("This loop will never end")