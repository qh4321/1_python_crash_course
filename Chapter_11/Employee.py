class Employee():

    def __init__(self, f_name, l_name, salary):
        self.first = f_name
        self.last = l_name
        self.salary = salary

    def give_raise(self, amount = 5000):
        self.salary += amount
