class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("\nThis restaurant " + self.name.title() + " has " + self.type + " type of cuisine.")

    def open_restaurant(self):
        print('This restaurant is now open!')
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, addition):
        self.number_served += addition

restaurant = Restaurant("Holly", 'deutsche')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print('\nNumber served: ' + str(restaurant.number_served))
restaurant.number_served = 430
print('Number served: ' + str(restaurant.number_served))

restaurant.set_number_served(1250)
print('Number served: ' + str(restaurant.number_served))

restaurant.increment_number_served(300)
print('Number served: ' + str(restaurant.number_served))
