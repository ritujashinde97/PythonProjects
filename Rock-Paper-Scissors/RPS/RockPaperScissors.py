import random


draws = 0
wins = 0
losses = 0
is_ended = False

print("\nLet's play Rock-Paper-Scissors !!! \n")
Prompt = "Choose Rock(r) , Paper(p) , Scissors(s)  or Quit(q) : "

while True :
    user_choice = input(Prompt)
    while user_choice not in ['r','p','s','q']:
        user_choice(input(Prompt))
    if user_choice == 'q':
        break
    else:
        comp_choice = random.choice(['r','p','s'])
        if comp_choice == 'r' :
            move = 'rock'
        elif comp_choice == 'p' :
            move = 'paper'
        else:
            move = 'scissors'

        print('Computer gives a ' +move)
        if comp_choice == user_choice :
            print("It's a Draw !")
            draws += 1
        elif(comp_choice =='r' and user_choice == 'p') or \
            (comp_choice == 'p' and user_choice == 's') or \
            (comp_choice == 's' and user_choice == 'r') :
            print('Woohooo!! You Win !!!')
            wins += 1

        else :
            print('Oops !!! You Loose !!!')
            losses +=1

print('You have ' + str(wins) + ' wins,' + str(draws) +' draws, and ' + str(losses) + ' losses .')



