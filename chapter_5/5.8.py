#5.8
users = ['Yuki', 'shiro', 'sakura', 'admin']
if users:
    for use in users:
        if use == 'admin':
            print('\nHello admin, would you like to see a status report?')
        else:
            print('\nHello ' + use + ', thank you for logging in again.')
else:
    print('\nWe need to find some users!')


#5.10
current_users = ['Keisuke', 'kuro', 'Nene', 'Masao', 'KAZAMA']
new_users = ['sara', 'momo', 'maSAO', 'kaZAma', 'ichi']
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('\nSorry ' + new_user + ', the name is already taken. ')
    else:
        print('\nGreat, ' + new_user + ' is still avaliable.')


#5.11
numbers = range(1,10)
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(str(number) + 'th')



