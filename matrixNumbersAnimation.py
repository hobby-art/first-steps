import random, sys, time

#Width of the animation
WIDTH = 70

try:
    #Setting the number of columns
    columns = [0] * WIDTH
    #Beginning the main loop
    while True:
        #Going through every column by sending WIDTH argument
        for i in range(WIDTH):
            #Assigning an item in the columns list a random number with 2% chance.
            if random.random() < 0.02:
                columns[i] = random.randint(4,14)
            
            #Checking if there is a number (which was assigned in the previous step). If there isn't, print empty space and end the line wihtout creating a new line.
            if columns[i] == 0:
                print(' ', end='')
            #If there IS a number, print 0 or 1 and decrease the number by 1 (when the number becomes 0, this column will not be printed).
            else:
                print(random.choice([0, 1]), end='')
                columns[i] -= 1
        #Print a new line and set time delay
        print()
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()