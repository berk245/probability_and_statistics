# Hey there, this is the first coding exercise!

# The objective of this exercise is to throw two unbiased dice and
# calculate the probability of getting an even score or one greater than 7.

import random
import numpy as np

# function for rolling the dice


def roll_dice(n_simulations=1000):
    count = 0

    # each repeat of the loop is another trial of the experiment
    for i in range(n_simulations):

        # roll die number #1
        die1 = random.randint(1, 6)  # fill in with min max die values

        # roll die number #2
        die2 = random.randint(1, 6)

        # sum the two values to get the score
        score = die1 + die2
        # if the score can be devided by 2 has no remainder OR is more than 7, add it to the count
        if not (score % 2) or score > 7:
            count = count + 1
    return (count/n_simulations)  # count divided by number of simulations


text = "The probability of rolling an even or greater number than 7 is "
print(text, np.round(roll_dice()*100, 2), "%")
