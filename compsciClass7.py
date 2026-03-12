#create a restaurant class, taking restaurantName and cuisineType
class Restaurant:
    def __init__(self,Name,Cuisine):
        self.name = Name
        self.cuisine = Cuisine
    def describe(self):
        print(f"{self.name} is a {self.cuisine} restaurant")
    def open(self):
        print(f"{self.name} is open")

#place = Restaurant("Mega Chicken","Nigerian")
#place.describe()
#place.open()
