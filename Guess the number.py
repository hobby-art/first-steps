import random

#Assign variables
secret_number = random.randint(1, 20)
guesses = 0

print('Guess the number from 1 to 20.')

#Input and check the number
while True:
    response = int(input('>'))
    if response > secret_number:
        print('Your number is too big.')
        continue
    elif response < secret_number:
        print('Your number is too small.')
        continue
    else:
        print('You are correct!')
        break
