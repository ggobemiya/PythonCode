# Codesignal>Arcade>Intro #51 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/26
# When I finish all Arcade, I can give a good answer.

def deleteDigit(n):
    M = 0
    k= []
    for i in range(len(str(n))):
        k.append(str(n)[i])
    for i in range(len(k)):
        k1 = k[:]
        del k1[i]
        m =int(''.join(k1))
        if m>M:
            M=m
    return M

