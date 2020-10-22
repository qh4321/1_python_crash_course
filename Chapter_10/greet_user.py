<<<<<<< HEAD
import json

filename = "username.json"

with open(filename) as f:
    username = json.load(f)
=======
import json

filename = "username.json"

with open(filename) as f:
    username = json.load(f)
>>>>>>> 0ad53dac9cd47facb93fdb57a08285ce5fa8b9e9
    print("Welcome back, " + username + '!')