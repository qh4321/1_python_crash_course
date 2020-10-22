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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type = 'ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def show_flavor(self):
        print("We have the following flavors avaliable: ")
        for flavor in self.flavors:
            print('  -' + flavor.title())

tataya = IceCreamStand('tataya')
tataya.flavors = ['valina', 'erdbeere', 'preffer', 'kaffe', 'ei']
tataya.describe_restaurant()
tataya.open_restaurant()
tataya.show_flavor()
    

    
    