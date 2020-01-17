def allLongestStrings(inputArray):
    k = []
    [k.append(len(inputArray[i])) for i in range(len(inputArray))]
    c = [inputArray[i] for i,x in enumerate(k) if x == max(k)]
    return c


# Codesignal>Arcade>Intro #9 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/15
# When I finish all Arcade, I can give a good answer.
