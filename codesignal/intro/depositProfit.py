# Codesignal>Arcade>Intro #31 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/07
# When I finish all Arcade, I can give a good answer.


def depositProfit(deposit, rate, threshold):
    i=0
    while deposit<threshold:
       deposit = deposit*(1+rate/100)
       i += 1
    return i
