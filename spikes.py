import time

#Assigning global variables
spikes = 0

#Main loop
while True:

    #Grow the spikes
    for i in range(1, 9):
        time.sleep(0.1)
        print('-' * (i * i))

    #Reduce the spikes
    for i in range(9, 1, -1):
        time.sleep(0.1)
        print('-' * (i * i))
