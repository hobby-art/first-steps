import time, sys

#Assigning global variables
indent = 0
indent_increasing = True

#Main loop
while True:
    #Format the print and set the time delay
    print(' ' * indent, end='')
    print('********')
    time.sleep(0.1)
    #Check how many indentations to add and to which direction to move
    if indent_increasing:
        indent = indent + 1
        if indent == 20:
            indent_increasing = False
    else:
        indent = indent - 1
        if indent == 0:
            indent_increasing = True
