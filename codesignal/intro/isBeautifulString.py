# Codesignal>Arcade>Intro #43 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/14
# When I finish all Arcade, I can give a good answer.

def isBeautifulString(inputString):
    ans = True
    k = []
    for i in range(26):
        k.append(inputString.count(chr(i+97)))
    for i in range(len(k)-1):
        if k[i]<k[i+1]:
            ans = False
    return ans

            
