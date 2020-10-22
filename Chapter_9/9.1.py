class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print("\nThis restaurant " + self.name.title() + " has " + self.type + " type of cuisine.")

    def open_restaurant(self):
        print('This restaurant is now open!')


restaurant = Restaurant("Holly", 'deutsche')
restaurant.describe_restaurant()
restaurant.open_restaurant()
