#6-3
#Think of five programming words. 
#Use these words as the keys in your glossary, and store their meanings as values.
glossary = {
    "Integer":"A whole number",
    "Float": "Data type used to represent numbers that have a decimal point. ",
    "String":"Characters within any quotations marks",
    "Boolean":"Data type representing 'True' or 'False'",
    "List":"A data type for storing ordered collections of items.",
    "Dictionary":"Stores data in a key:value pair",
    "Tuple":"An ordered sequence of elements that is immutable",
    "Character":"An individual character, e.g. 'w', '@'"
}
#print each word and its meaning
print (f"Integer : {glossary['Integer']}")
print (f"\nFloat : {glossary['Float']}")
print (f"\nString : {glossary['String']}")
print (f"\nBoolean : {glossary['Boolean']}")
print (f"\nList : {glossary['List']}")
print ("\n ")
#6-4
#print each word and meaning using a for loop
#go back to the glossary and add 3 more words
for key, value in glossary.items():
    print (f"{key} : {value}")
    print ("\n")
print ("\n ")

#6-5
#Make a dictionary with three rivers as keys and the country where the river is as values
rivers = {
    "Nile" : "Egypt",
    "Benue" : "Nigeria and Cameroon",
    "Ruki" : "Democratic Republic of Congo"
}
#print a sentence about each river using key & value and a loop
for key, value in rivers.items():
    print (f"The River {key} runs through {value}.")
print (" ")
#print the name of each river using a for loop
for key in rivers.keys():
    print (key)
print (" ")
#print the name of each country using a for loop
for value in rivers.values():
    print (value)
print ("\n ")

#6-6
#code below given in question
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
#Make a list of people using some of the names in the dictionary
participants = ["jen","ayomide","sarah","chidubem","edward","hanifat","phil"]
#loop through participants, if they have taken the poll thank them, otherwise ask them to take the poll
for person in participants:
    if person in favorite_languages:
        print (f"\nThank you {person.title()}, for taking the poll!")
    else:
        print (f"\n{person.title()}, please take the poll.")
print ("\n ")

#6-7
#Make 3 dictionaries for different people
person1 = {
    "firstName" : "LeBron",
    "lastName" : "James",
    "age" : 41,
    "city" : "Los Angeles"
}

person2 = {
    "firstName" : "Kevin",
    "lastName" : "Durant",
    "age" : 37,
    "city" : "Houston"
}

person3 = {
    "firstName" : "Victor",
    "lastName" : "Wembanyama",
    "age" : 22,
    "city" : "San Antonio"
}
#store all dictionaries in a list
people = [person1,person2,person3]

#use a for loop and print all the information
for person in people:
    for v in person.values():
        print (v)
    print("\n")

#6-8
#make 3 dictionaries for 3 different pets
pet1 = {
    "name" : "leo",
    "species" : "dog",
    "owner" : "david"
}

pet2 = {
    "name" : "patches",
    "species" : "cat",
    "owner" : "sarah"
}

pet3 = {
    "name" : "goldie",
    "species" : "goldfish",
    "owner" : "alex"
}

#store the dictionaries in a list
pets = [pet1,pet2,pet3]
#print the information
for pet in pets:
    for k,v in pet.items():
        print (f"{k.title()} : {v.title()}")
    print("\n")
