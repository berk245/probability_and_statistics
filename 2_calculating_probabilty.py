# Week 2 of exercises, this time we have an introduction to calculating
# probabilities.

# "A box contains 10 white balls, 20 reds and 30 greens. Draw 5 balls with replacement
# what is the probability that:
# 3 white or 2 red
# all 5 are the same color"

import random
import numpy as np


# set up a dictionary that we will use for this problem out of which we can draw a random color

# add into this dictionary
# 10 white balls
# 20 reds
# 30 greens
# A function that returns a dictionary that fits to the problem requirements

def make_dictionary():
    result = {}
    array = []
    # Create an array with required amount of balls
    for i in range(1, 61):
        if i < 11:
            array.append('white')
        elif i < 31:
            array.append('red')
        else:
            array.append('green')
    # Shuffle the array to make it more random
    random.shuffle(array)

    # Create a dictionary with indexes.
    # This step is added only because the solution suggested a dictinary
    for index, color in enumerate(array):
        result[index] = color
    return (result)


d = make_dictionary()

# initializing the important variables
n_simulations = 100000
part_a_total = 0
part_b_total = 0

for i in range(n_simulations):

    # make a list of the colors we chose
    chosen_colors = []

    # append the 5 draws to the list from the 60 choice dictionary
    for i in range(5):
        chosen_colors.append(d[random.randrange(0, 60)])

    # convert it to a numpy array
    our_list = np.array(chosen_colors)

    # find the number of each that we picked
    white = sum(our_list == "white")
    red = sum(our_list == "red")
    green = sum(our_list == "green")

    # keep track of if the combinations met the 2 criterias
    # if white = 3 and red = 2, add it to part_a_total
    if white == 3 and red == 2:
        part_a_total = part_a_total + 1

    # if red is 5 and white is 5 or green is 5 add it to part_b_total
    if red == 5 or white == 5 or green == 5:
        part_b_total = part_b_total + 1


print("The probability of drawing 3 white and 2 red balls is ",
      part_a_total/n_simulations*100, "%")
print("the probability of drawing all 5 of the same color is ",
      part_b_total/n_simulations*100, "%")
