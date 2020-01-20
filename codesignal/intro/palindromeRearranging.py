# Codesignal>Arcade>Intro #18 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/20
# When I finish all Arcade, I can give a good answer.

def palindromeRearranging(inputString):
    ans = False
    if len(inputString)==1:
        ans = True
    elif len(inputString)%2 == 0:
        a= list(set(inputString))
        for i in range(len(a)):
            if inputString.count(a[i])%2 ==1:
                break
            ans = True
    elif len(inputString)%2 == 1:
        a= list(set(inputString))
        k = 0
        for i in range(len(a)):
            b = inputString.count(a[i])%2
            k += b
        if k == 1:
            ans = True
    return ans
