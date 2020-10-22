## greet_users
def greet_users(names):
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

usernames = ['herry', 'lili', 'yaya']
greet_users(usernames)


# printing_models

unprinted_desighs = ['iphone case', 'robot', 'dodedode kakaka']
completed_design = []

while unprinted_desighs:
    current_design = unprinted_desighs.pop()
    print("Printing model: " + current_design)
    completed_design.append(current_design)

print("\nThe following models have been printed: ")
for model in completed_design:
    print(model)


# 

def print_models(unprinted_models, completed_models):

    while unprinted_models:
        current_design = unprinted_models.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def  show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_models = ['iniahc', 'shue cjshwu', 'schhcdch']
completed_models = []

print_models(unprinted_models, completed_models)
show_completed_models(completed_models)