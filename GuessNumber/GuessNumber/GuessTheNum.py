import random

playercomp = 'y'

while(playercomp == 'y'):
    answer = random.randint(1,100)
    try_number = input('Guess the number between 1 to 100:')
    try_number = int(try_number)
    counter = 1

    while answer != try_number:
        if try_number > answer :
            print('Your number is too large')

        if try_number < answer :
            print('Your number is too small')

        try_number = int(input('Guess the number between 1 to 100:'))
        counter = counter+1
    print('You got it!!! You tried ' +str(counter) + 'times')

    playercomp = input('Continue y/N ?')

