<<<<<<< HEAD
import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What's your name? ")
    filename = "username.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
    
def greet_user():
    username = get_stored_username()
    if username:
        correct = input("Are you " + username + '?(y/n) ')
        if correct == 'y':
            print("Welcome back, dear " + username + '.')
        else:
            username = get_new_username()
            print("We'll remember you when you come back, dear " + username + '.')
    else:
        username = get_new_username()
        print("We'll remember you when you come back, dear " + username + '.')

greet_user()
=======
import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What's your name? ")
    filename = "username.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
    
def greet_user():
    username = get_stored_username()
    if username:
        correct = input("Are you " + username + '?(y/n) ')
        if correct == 'y':
            print("Welcome back, dear " + username + '.')
        else:
            username = get_new_username()
            print("We'll remember you when you come back, dear " + username + '.')
    else:
        username = get_new_username()
        print("We'll remember you when you come back, dear " + username + '.')

greet_user()
>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
