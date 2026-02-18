#7-9
#use the list snack_orders from the previous question
snack_orders = ["meatpie","fishpie","chickenpie","meatpie","donut","sausage roll","meatpie"]
#make sure a snack appears 3 times
#print a message telling the user we have run out of "meatpie"
print("We have run out of meatpie")
#remove all instances of meatpie using a while loop
while "meatpie" in snack_orders:
    snack_orders.remove("meatpie")
#make sure there is no "meatpie" remaining 
print (snack_orders)