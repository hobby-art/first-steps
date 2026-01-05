#Defining function to check the number
def collatz(number):
    if number % 2 == 0:
        print(number // 2, end=' ')
        return number // 2
    else:
        print(3 * number + 1, end=' ')
        return 3 * number + 1

#Collatz loop
while True:
    try:
        print('') #Can't start "Your number" from the new line after first use. Using this workaround.
        print('Your number: ')
        user_number = int(input('>'))
        result = collatz(user_number)
        while result != 1:
            result = collatz(result)
    #Checking if user gave string input
    except ValueError:
        print('Write a number.')
