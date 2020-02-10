# Codesignal>Arcade>Intro #33 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/10
# When I finish all Arcade, I can give a good answer.



from itertools import permutations

def diff(w1, w2):
        return sum([a[0] != a[1] for a in zip(w1, w2)]) == 1

def stringsRearrangement(inputArray):
    for z in permutations(inputArray):
        if sum([diff(*x) for x in zip(z, z[1:])]) == len(inputArray) - 1:
            return True
    return False
#문제이해가 안된다
