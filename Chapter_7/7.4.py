prompt = "\nWhat would you like on your pizza? "
prompt += "\nEnter 'quit' if you are finished. "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("I'd add " + topping  + " in the pizza.")
    else:
        break