# Codesignal>Arcade>Intro #47 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/19
# When I finish all Arcade, I can give a good answer.

def isMAC48Address(inputString):
    ans = False
    if len(inputString) != 17 or inputString.count("-")!=5:
        ans = False
    elif len(inputString) == 17 and inputString.count("-")==5:
        for i in [0,1,3,4,6,7,9,10,12,13,15,16]:
            if 48<=ord(inputString[i])<=57 or 65<=ord(inputString[i])<=70:
                ans = True
            else : 
                return False
           # print(i)
    return ans
