# this is the sample poker game using 3 dice
# with the implementation of python oneliner else if ladder with  PYTHON DICTIONARY

import random

die1, die2, die3 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)

# this method uses the dictionary to map the values corresponding to the condition.
value = {(die1 == die2 and die2 == die3): "Three of a kind", (die1 == die2 or die2 == die3 or die1 == die3): "1Pair"}.get(True, "Better luck next time!")

print(value)
