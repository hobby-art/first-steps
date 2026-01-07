import random


# Function to make 100 flips and save the result in the list.
def flips():

    heads_or_tails = []

    for i in range(100):
        if random.randint(0, 1) == 0:
            heads_or_tails.append("H")
        else:
            heads_or_tails.append("T")

    return heads_or_tails


# Function to check if the list of flips has streaks.
def streaks(list):

    streaks_num = 0

    for i in range(len(list)):
        if list[i : i + 6] == ["H"] * 6 or list[i : i + 6] == ["T"] * 6:
            streaks_num += 1
            break

    return streaks_num


# Sum of streaks of the following loop.
number_of_streaks = 0

# Repeat the flips and check the streaks for 10,000 times.
for i in range(10000):
    number_of_streaks += streaks(flips())

# Calculate and print the percentate of streaks.
print("Chance of streak: %s%%" % (number_of_streaks / 100))
