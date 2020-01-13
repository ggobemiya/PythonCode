def adjacentElementsProduct(inputArray):
    b=[]
    for i in range(len(inputArray)-1):
        k=inputArray[i]*inputArray[i+1]
        b.append(k)
    return max(b)

# Codesignal>Arcade>Intro #4 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/13
# When I finish all Arcade, I can give a good answer.
