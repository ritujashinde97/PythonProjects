import random


play_game = 'y'
start = 1
end = 100
direction = 'N'
smallest = start
largest = end

while play_game == 'y':
    smallest = start
    largest = end
    print('Guess the number between 1 to 100 : ')
    try_number = random.randint(start,end)
    print(try_number)
    counter = 0
    direction = 'N'

    while direction != 'C':
        direction=(input('is it too large(L) or too small(S) or correct (C)?'))
        if direction == 'S':
            try_number > smallest
            smallest = try_number + 1
        try_number = random.randint(smallest, largest)
        print(try_number)

        if direction == 'L':
            try_number < largest
            largest = try_number - 1
        try_number = random.randint(smallest, largest)
        print(try_number)
        counter=counter + 1
    print('I got it.. I tried  ' +str(counter) +'times')
    play_game = input('continue? y/n')