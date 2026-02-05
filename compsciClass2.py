#Think of 3 types of pizza, store in list and use a for loop to print each name
pizzas = ["pepperoni","suya","cheese"]
for pizza in pizzas:
    print(pizza)
#have a for loop print a sentence containing the name of each pizza
for pizza in pizzas:
    print(f"I like {pizza} pizza")
#Have a line removed from the loop about how much I love pizza
print("I really love pizza")

#store the names of 3 animals in a list and a for loop to print each name
animals = ["cow","goat","chicken"]
for animal in animals:
    print(animal
#print a statement about each animal in a for loop
for animal in animals:
    print (f"a {animal} is a farm animal")
#add a line, stating what these animals have in common
print ("They are all regularly eaten")


make a list 1 - 1000000
make an empty list
one_million = []
#use for loop to append the digits into the list
for value in range(1,1001):
    one_million.append(value)

#use min() and max() on the list
print(min(one_million))
print(max(one_million))
print(sum(one_million))

#make a list of odd numbers from 1-20 and print each number
odd_numbers = []
for value in range(1,20,2):
    odd_numbers.append(value)
print(odd_numbers)

#make a list of multiples of three and print 
multiplesThree = []
for value in range(3,31,3):
    multiplesThree.append(value)
print(multiplesThree)

#make a list of cubes from 1-10 using a for loop, and print the list
cubes=[]
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

#cubes list comprehension
cubess = [val**3 for val in range(1,11)]
print(cubess)
#print the first three items in the list
print (f"The first three items in the list are {cubess[0:3]}")
#print three items from the middle of the list
print (f"The three items from the middle of this list are {cubess[3:6]}")
#print the last three item from this list
print (f"The last three items from this list are {cubess[7:]}")

age = 17
if age<=4:
    print ("Your ticket is $0")
elif age<=18:
    print ("Your ticket is $25")
else:
    print ("Your ticket is $40")


