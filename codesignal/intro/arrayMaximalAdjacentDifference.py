# Codesignal>Arcade>Intro #20 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/21
# When I finish all Arcade, I can give a good answer.


def arrayMaximalAdjacentDifference(inputArray):
    i=0
    ans = 0
    while i < len(inputArray)-1:
        ans1 = abs(inputArray[i]-inputArray[i+1])
        if ans1> ans:
            ans = ans1
        i +=1
    return ans
    
    
