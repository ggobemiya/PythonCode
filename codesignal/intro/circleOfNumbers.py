Learn more or give us feedback
# Codesignal>Arcade>Intro #30 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/07
# When I finish all Arcade, I can give a good answer.

def circleOfNumbers(n, firstNumber):
    if int(n/2)>firstNumber:
        ans = list(range(n))[int(n/2):][list(range(n))[:int(n/2)].index(firstNumber)]
    else:
        ans = list(range(n))[:int(n/2)][list(range(n))[int(n/2):].index(firstNumber)]
    
    return ans
