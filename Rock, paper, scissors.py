import random

#Assigning the global variables
wins = 0
losses = 0
ties = 0

#Main loop
while True:
    #Assign the item to the computer
    comp_item = ''
    comp = random.randint(1,3)
    if comp == 1:
        comp_item = 'r'
        print('My item is r')
    elif comp == 2:
        comp_item = 'p'
        print('My item is p')
    else:
        comp_item = 's'
        print('My item is s')

    #Ask for the input and save it in the variable
    print('What are you playing: r, p or s? Write "q" to quit')
    my_item = input('>')

    #Check the quit
    if my_item == 'q':
        print('Bye!')
        break

    #Check the input
    if my_item != 'r' and my_item != 'p' and my_item != 's':
        print('Write correctly. Try again.')
        continue

    #Compare computer's item with the player's item

    #Cecking ties
    if comp_item == my_item:
        ties = ties + 1
        print('It is a tie!')
        print('Wins: ' + str(wins) + ', Losses: ' + str(losses) + ', Ties: ' + str(ties))
        continue

    #Checking wins
    if my_item == 'r' and comp_item == 's':
        wins = wins + 1
        print('You won!')
        print('Wins: ' + str(wins) + ', Losses: ' + str(losses) + ', Ties: ' + str(ties))
        continue
    elif my_item == 'p' and comp_item == 'r':
        wins = wins + 1
        print('You won!')
        print('Wins: ' + str(wins) + ', Losses: ' + str(losses) + ', Ties: ' + str(ties))
        continue
    elif my_item == 's' and comp_item == 'p':
        wins = wins + 1
        print('You won!')
        print('Wins: ' + str(wins) + ', Losses: ' + str(losses) + ', Ties: ' + str(ties))
        continue

    #Checking losses
    if my_item == 'r' and comp_item == 'p':
        losses = losses + 1
        print('You lost!')
        print('Wins: ' + str(wins) + ', Losses: ' + str(losses) + ', Ties: ' + str(ties))
        continue
    elif my_item == 'p' and comp_item == 's':
        losses = losses + 1
        print('You lost!')
        print('Wins: ' + str(wins) + ', Losses: ' + str(losses) + ', Ties: ' + str(ties))
        continue
    elif my_item == 's' and comp_item == 'r':
        losses = losses + 1
        print('You lost!')
        print('Wins: ' + str(wins) + ', Losses: ' + str(losses) + ', Ties: ' + str(ties))
        continue
