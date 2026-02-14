#dictionary called favourite places, use names as keys and places as values
favourite_places = {
    "adeboye" : ["shop","park","office"],
    "bolanle" : ["pitch","bank","hospital"],
    "chukwuemeka" : ["mall","court","school"]
}

#loop and print key and values
for name,places in favourite_places.items():
    allplaces = ""
    #Adeboye's favourite places are shop,park,office
    for place in places:
        allplaces += place + ", "
    print(f"{name.title()}'s favourite places are: {allplaces}")
    print (" ")

#Adeboye's favourite places are:
#shop
#park
#office
for name,places in favourite_places.items():
    print (f"{name.title()}'s favourite places are:")
    for place in places:
        print(place)
    print(" ")

#store 5 names as keys and 2 numbers as values for each key
favourite_nums = {
    "emma" : [24,31],
    "sarah" : [71,95],
    "hannah" : [34,68],
    "daryl" : [9,42],
    "blayre" : [17,56]
}
#print each name and number
for name,nums in favourite_nums.items():
    print(f"{name.title()}'s favourite numbers are:")
    for num in nums:
        print (num)
    print (" ")

#city = {name:{country:,population:,fact:}}
city = {
    "Lagos" : {
        "country" : "nigeria",
        "population" : 17000000,
        "fact" : "has the second-highest gdp in africa"
    },
    "Niamey" : {
        "country" : "niger",
        "population" : 978000,
        "fact" : "is niger's main economic centre"
    },
    "N'Djamena" : {
        "country" : "chad",
        "population" : 807000,
        "fact" : "was called fort lamy by colonisers"
    }
}
#print name of city and information
#Lagos is in nigeria, has a population of 17mil and has the second-highest gdp in africa
for k,v in city.items():
    print (f"{k} is in {v["country"].title()}, has a population of {v["population"]} and {v["fact"]}")