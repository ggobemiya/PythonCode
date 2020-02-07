# Codesignal>Arcade>Intro #32 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/07
# When I finish all Arcade, I can give a good answer.

def absoluteValuesSumMinimization(a):
    ans = 999999999999
    s = 0
    ans1 = 0
    for i in range(len(a)):
        for j in range(len(a)):
            ans1 += abs(a[i]-a[j]) 
        if ans > ans1:
            ans = ans1
            s = i
        ans1 = 0    
    return a[s]
