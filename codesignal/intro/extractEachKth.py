# Codesignal>Arcade>Intro #34 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/10
# When I finish all Arcade, I can give a good answer.


def extractEachKth(inputArray, k):
    leng = len(inputArray)
    s1 = leng//k
    a = list(range(k-1,len(inputArray),k))
    for i in a[::-1]:
        del inputArray[i]
    return inputArray
