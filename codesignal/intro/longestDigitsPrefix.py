# Codesignal>Arcade>Intro #40 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/14
# When I finish all Arcade, I can give a good answer.

def longestDigitsPrefix(inputString):
    ans = ''
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            ans += inputString[i]
        else:
            break
    if range(len(ans))==1:
        return ""
    return ans
        
