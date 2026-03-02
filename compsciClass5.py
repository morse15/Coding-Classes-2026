#let the user add pizza toppings until they 'quit'
# pizzaToppings  = []
# toppings = ""
# active = True
# print("Please enter your required toppings one by one")
# print("When you are done type 'quit' in the terminal")
# while active:
#     toppings = input("Topping: ")
#     toppings = toppings.lower()
#     toppings = toppings.strip()
#     print(f"We'll add {toppings}")
# #    pizzaToppings.append(toppings)
#     if toppings == "quit":
#         active = False

# print("\n")
# print ("Your pizza topping are below:")
# for pizzaTopping in pizzaToppings:
#     print(pizzaTopping)
# print("\n")


#print("Hello World")
#Make a list called snack_orders and fill it with the names of various snacks.
snack_orders = ["meatpie","fishpie","chickenpie","donut","sausage roll"]
#make an empty list called finished_snacks
finished_snacks = []
#loop through and print a message for each order, move the order from snack_orders to finished_snacks. 
while snack_orders:
    order = snack_orders[-1]
    finished_snacks.append(order)
    snack_orders.remove(order)
#print a message listing all the snacks that were made
print("These are the snacks that were made:")
for snack in finished_snacks:
    print(snack)

#poll users about their dream vacation
poll = {}
while True:
    name = input("\nWhat is your name?: ")
    dreamVacation = input("\nIf you could visit one place in the world where would you go?: ")
    poll[name.title()] = dreamVacation.title()
    again = input("\nIs anyone else going to answer this poll?(Y/N): ")
    again = again.upper()
    if again == ("N"):
        break
#print each answer to the poll
for names,dreams in poll.items():
    print(f"{names}'s dream vacation is in {dreams}")

