# Codesignal>Arcade>Intro #25 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/28
# When I finish all Arcade, I can give a good answer.


def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i in range(len(inputArray)):
        if inputArray[i]==elemToReplace:
            inputArray[i]=substitutionElem
    return inputArray
