# Codesignal>Arcade>Intro #17 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/20
# When I finish all Arcade, I can give a good answer.

def arrayChange(inputArray):
    ans=0
    i=0
    while i < len(inputArray)-1:
        if inputArray[i]>=inputArray[i+1]:
            k = inputArray[i]-inputArray[i+1]
            inputArray[i+1] = inputArray[i]+1
            ans = ans+k+1
        else:
            i+=1
    return ans
