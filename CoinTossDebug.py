import random, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s - %(message)s')

guess = ''

#Ask for input and check it
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

#toss = random.randint(0, 1) # 0 is tails, 1 is heads - incorrect line from the book

#Making a toss and checking it with the input
if random.randint(0, 1) == 0:
    toss = 'tails'
    logging.debug('Toss is tails.')
else:
    toss = 'heads'
    logging.debug('Toss is heads.')

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
