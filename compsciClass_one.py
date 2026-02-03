#3-3. Your Own List: Think of your favorite mode of transportation, such as a
#motorcycle or a car, and make a list that stores several examples. Use your list
#to print a series of statements about these items, such as “I would like to own a
#Honda motorcycle.”

transport = ['Honda', 'Suzuki', 'Toyota', 'Lexus', 'Camry']
print(f"I would like to own a {transport[0]} car")
print(f"My favourite car brand is {transport[4].upper()}")
print(f"My favourite car brand is {transport[-1]}")

print (transport)

#I would create a guest list and add 3 names to it
#Print a message stating "Hello [Guest], you are invited to dinner at my house."
guestList = ['Adam', 'Eve', 'Abel']
print(f"Hello {guestList[0]}, you are invited to dinner")
print(f"Hello {guestList[1]}, you are invited to dinner")
print(f"Hello {guestList[2]}, you are invited to dinner")

#print Abel won't be coming
#replace Abel with Cain
#print a message stating "Hello [Guest], you are invited to dinner"
print(f"{guestList[2]} is unable to make it")
guestList[2] = "Cain"
print(f"Hello {guestList[0]}, you are invited to dinner")
print(f"Hello {guestList[1]}, you are invited to dinner")
print(f"Hello {guestList[2]}, you are invited to dinner")

#inform guests that I found a bigger table. 
#insert 1 newGuest to beginning of the list
#insert 1 newGuest to middle of the list
#append 1 newGuest to end of the list
#invite anew

print ("I have found a bigger table")
guestList.insert(0,"Ayo")
guestList.insert(2, "David")
guestList.append("Blessing")
print(f"Hello {guestList[0]}, you are invited to dinner")
print(f"Hello {guestList[1]}, you are invited to dinner")
print(f"Hello {guestList[2]}, you are invited to dinner")
print(f"Hello {guestList[3]}, you are invited to dinner")
print(f"Hello {guestList[4]}, you are invited to dinner")
print(f"Hello {guestList[5]}, you are invited to dinner")

#I can only invite two people, sorry
#pop name, apologise
#tell those remaining that they are still invited. 
#delete and make list empty

print("I can only invite two people, sorry")
popped_guest = guestList.pop()
print (f"Unfortunately, {popped_guest} you have been uninvited from dinner.")
popped_guest = guestList.pop()
print (f"Unfortunately, {popped_guest} you have been uninvited from dinner.")
popped_guest = guestList.pop()
print (f"Unfortunately, {popped_guest} you have been uninvited from dinner.")
popped_guest = guestList.pop()
print (f"Unfortunately, {popped_guest} you have been uninvited from dinner.")

print(f"{guestList[0]}, you are still invited to dinner")
print(f"{guestList[1]}, you are still invited to dinner")

del guestList[1]
del guestList[0]
print (guestList)
