# Sample list.
spam = ["apples", "bananas", True, "tofus", "cats", 42]


# Function to convert a list into a string where values are separated by a comma and with the word "and" before the last value.
def listWrangler(list):

    # Checking if the list is empty.
    if len(list) == 0:
        print("The list is empty.")
        return

    # Creating the string variable and assigning to it the first item from the list.
    listString = str(list[0])

    # Adding remaining items of the list into a string. Also converting other than a string types of values into a string.
    for item in list[1:]:
        if item != list[-1]:
            listString = listString + ", " + str(item)
        else:
            listString = listString + " and " + str(item)

    # Printing the result.
    print(listString)


listWrangler(spam)
