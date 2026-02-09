#Make a list of five usernames
usernames = ["admin","ghost34","flash47","water51","round_metal3"]
#loop through the list and greet each user
if usernames:
    for user in usernames:
        #if user is Admin, print special greeting
        if user == "admin":
            print("Hello Admin, would you like to see a status report")
        else:
            print(f"Welcome {user.title()}, thank you for logging in again.")
#if list is empty, print ("We need to find some users")
else: 
    print("We need to find some users")
#Make a list of usernames called current_users
current_users = ["bland_attack71","chairperson926","plankist4","draginto63","vroooommm"]
#make a list of new users with some overlap
new_users = ["John","James","Jeremy","Chairperson926","plankist4"]

#create a copy to allow for the test to be case insensitive
new_users_copy = []
for copy in new_users:
    new_users_copy.append(copy.lower())
print (new_users_copy)
#loop through making sure the new_users names are available, remember to be case insensitive
for n_user in new_users_copy:
    if n_user in current_users:
        print ("This username is unavailable")
    else:
        print ("You may proceed")
print ("\n ")

#store 1-9 in a list
ordinal = [1,2,3,4,5,6,7,8,9]
#loop through the list
#Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
for num in ordinal:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print (f"{num}th")
print ("\n ")

#use a dictionary to store first name, last name, number and city of a person
person = {
    "first_name" : "Emma",
    "last_name" : "Maltais",
    "number" : 27,
    "city" : "Toronto"
}
#print each attribute
print(person["first_name"].upper())
print(person["last_name"].upper())
print(person["age"])
print(person["city"])
print("\n ")

#store five name with five numbers in a dictionary
numbers = {
    "morse" : 15,
    "Hannah Miller" : 34,
    "Daryl Watts" : 9,
    "Laura Stacey" : 7,
    "Emily Clark" : 26
}
#print each persons name and number
print(numbers)