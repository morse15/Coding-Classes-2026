#write a function called displayMessage that prints that I am learning about functions
def displayMessage():
    print("Today, we are learning about functions")
displayMessage()

#Write a function called favourite book which accepts a title parameter. In the function print a message about a book
def favBook(title):
    print(f"\nMy favourite book is {title}")
favBook("Holes")

#write a function that collects the size of a shirt and the text to be printed on it.
def shirts(size,text):
    print(f'\nThis shirt is a size {size} and has the text "{text}" printed on it.')
#call the function using positional arguments
shirts("Medium","Hello World!")
#call the function using keyword arguments
shirts(size = "Medium",text = "Hello World!")

#modify the code so that the shirts are large by default and the text reads "I love python"
def shirts1(size = "Large",text = "I love Python!"):
    print(f'\nThis shirt is a size {size} and has the text "{text}" printed on it.')
#call the function
shirts1()
#call the function and change the default
shirts1("Small","I hate Python!")

#make a function that says "[city] is in [country]"
#give the country a default value
def cities(city,country = "Nigeria"):
    print(f"{city.title()} is in {country.title()}")
cities("Lagos")
cities("Abuja")
cities("Cairo","Egypt")

#make a function that prints "[city],[country]"
def cityCountry(city,country):
    return f"\n{city}, {country}"

answer = cityCountry("Cairo","Egypt")
print(answer)
answer1 = cityCountry("","")
print(answer1)

#make a list containing a series of short text messages.
texts = ["Hello","Hi","How are you","I'm alright","...","...","Goodbye","Bye"]
#create a function to print each message
def messages(lists):
    for list in lists:
        print (list)

messages(texts)

#write a function that accepts any number of toppings 
def sandwich(*toppings):
    print ("These are the toppings you've chosen")
    for top in toppings:
        print(top)

sandwich("pepperoni","blah","blue","bluh")