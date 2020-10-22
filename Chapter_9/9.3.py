class User():
    def __init__(self, first_name, last_name, user_name, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.user_name = user_name
        self.email = email
        self.location = location.title()
    
    def describe_user(self):
        print("\nName: " + self.first_name + ' ' + self.last_name)
        print("User name: " + self.user_name)
        print("E-mail: " + self.email)
        print('Location: ' + self.location)

    def greet_user(self):
        print("Welcome back, " + self.user_name + '!')


user1 = User('Andy', 'nan', 'liliba', '12345@qq.com', 'aachen' )
user1.describe_user()
user1.greet_user()

