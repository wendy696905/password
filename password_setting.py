password = 'a123456'
chances = 3 #chances remain
while chances != 0:
    password_setting = input('Please enter your password: ')
    if password_setting == password:
        print('Login Successfully!')
        break
    else:
        chances = chances - 1
        if chances > 0:
            print('Please try again.', chances, 'chance remain.')
if chances == 0:
    print('No chance remain!')

        
