# Codesignal>Arcade>Intro #26 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/03
# When I finish all Arcade, I can give a good answer.


def evenDigitsOnly(n):
    ans = True
    for i in range(len(str(n))):
        if int(str(n)[i])%2 !=0:
            ans = False
    return ans
