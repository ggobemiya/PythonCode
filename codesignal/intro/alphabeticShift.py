# Codesignal>Arcade>Intro #28 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/05
# When I finish all Arcade, I can give a good answer.

def alphabeticShift(inputString):
    ans = []
    for i in range(len(inputString)):
        if inputString[i] == 'z':
            ans.append('a')
        else:
            ans.append(chr(ord(inputString[i])+1))
    ans1 = ''
    for j in range(len(ans)):
        ans1 += ans[j]
    return ans1
