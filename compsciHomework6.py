#8-7
#write a function that uses a dictionary to build an album using artist and album name
def make_album(artist, album,numSongs = None):
    musicAlbum = {
        "artistName" : artist,
        "albumName" : album
    }
    if numSongs:
        musicAlbum["songs"] = numSongs
    return musicAlbum
#use the function to create 3 albums
test = make_album("TV Girl","Who Really Cares")
print (test)
test1 = make_album("Chris Casey","Buried Out Back")
print (test1)
test2 = make_album("Lincoln","A Constant State of Ohio")
print (test2)
#add a way for songs to be added using 'None'
#add another album and add the number of songs
album3 = make_album("BROCKHAMPTON","GINGER",12)

#8-8
#use a while loop to let users add to the dictionary until they're ready to quit
while True:
    print("\nType 'q' at any point to quit")
    artist1 = input("Who is the artist for this album? : ")
    if artist1.lower() == "q":
        break
    album1 = input("\nWhat is the name of this album? : ")
    if album1.lower() == "q":
        break
    songs = input("\n How many songs are on the album? : ")
    if songs.lower() == "q":
        break
    end = make_album(artist1,album1,songs)
    print (end)

#8-10
#copy 8-9
texts = ["Hello","Hi","How are you","I'm alright","...","...","Goodbye","Bye"]
#create a function to print each message
# def messages(lists):
#     for list in lists:
#         print (list)
# #write a function that prints each message
# messages(texts)
#move each message to a new list as it is printed
sentMessages = []
def sendMessages(lists1):
    for text in lists1:
        a = text
        print (a)
        sentMessages.append(a)
        texts.remove(a)
sendMessages(texts)
    
#8-11

#8-14
#write a function that stores info about a car in a dictionary
def makeCar(manufacturer, modelName,**car):
    car["manufacturer"] = manufacturer
    car["model"] = modelName
    return car
#test the code using what's given in the question
car1 = makeCar("subaru","outback",color = "blue",tow_package = True)
print (car1)
