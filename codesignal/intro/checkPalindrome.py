def checkPalindrome(inputString):
    if len(inputString) == 1:
        return True
    elif len(inputString)%2 == 0:
        evennum = []
        for i in range(int(len(inputString)/2)):
            if inputString[i] == inputString[len(inputString)-1-i]:
                evennum.append(1)
            else:
                evennum.append(0)
        if sum(evennum) == int(len(inputString)/2):
            return True
        else:
            return False
    elif len(inputString)%2 == 1:
        oddnum = []
        for i in range(int(len(inputString)/2)):
            if inputString[i] == inputString[len(inputString)-1-i]:
                oddnum.append(1)
            else:
                oddnum.append(0)
        if sum(oddnum) == int(len(inputString)/2):
            return True
        else:
            return False 

# It was my first try.            

def checkPalindrome(inputString):
    if inputString == inputString[::-1]
        return True
    return False
    
# That was other answer after stury about list.

def checkPalindrome(inputString):
    return inputString == inputString[::-1]

# Best answer




# Codesignal>Arcade>Intro #3 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/13
# When I finish all Arcade, I can give a good answer.
