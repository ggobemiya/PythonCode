# Codesignal>Arcade>Intro #21 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/21
# When I finish all Arcade, I can give a good answer.


def isIPv4Address(inputString):
    splt = inputString.split(".")
    return len(splt) == 4 and all(i.isdigit() and 0<=int(i)<=255 for i in splt)
    
