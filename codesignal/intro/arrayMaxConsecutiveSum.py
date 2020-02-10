# Codesignal>Arcade>Intro #37 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/10
# When I finish all Arcade, I can give a good answer.


def arrayMaxConsecutiveSum(inputArray, k):
    max_v = sum(inputArray[0:k])
    l = len(inputArray)
    last_v = max_v
    for i in range(k, l):
        last_v = last_v+inputArray[i]-inputArray[i-k]
        if max_v < last_v:
            max_v = last_v
    return max_v
