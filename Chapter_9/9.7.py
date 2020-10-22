class User():
    def __init__(self, first_name, last_name, user_name, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.user_name = user_name
        self.email = email
        self.location = location.title()
        self.login_attempts = 0
    
    def describe_user(self):
        print("\nName: " + self.first_name + ' ' + self.last_name)
        print("User name: " + self.user_name)
        print("E-mail: " + self.email)
        print('Location: ' + self.location)

    def greet_user(self):
        print("Welcome back, " + self.user_name + '!')
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, user_name, email, location):
        super().__init__(first_name, last_name, user_name, email, location)
        self.privileges = []

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print('  -' + privilege)


user1 = Admin('Andy', 'nan', 'liliba', '12345@qq.com', 'aachen' )
user1.describe_user()
user1.greet_user()

user1.privileges = ['can add post', 'can delete post', 'can ban user']
user1.show_privileges()