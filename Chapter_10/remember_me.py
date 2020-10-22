<<<<<<< HEAD

import json

def greet_user():

    filename = "username.json"

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What's your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print("We'll remember you when you come back, " + username + '!')
    else:
        print("Welcome back, " + username + '!')

greet_user()
=======

import json

def greet_user():

    filename = "username.json"

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What's your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print("We'll remember you when you come back, " + username + '!')
    else:
        print("Welcome back, " + username + '!')

greet_user()
>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
