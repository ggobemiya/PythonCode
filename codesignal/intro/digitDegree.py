# Codesignal>Arcade>Intro #41 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/14
# When I finish all Arcade, I can give a good answer.

def digitDegree(n):
    ans=0
    if len(str(n))==1:
        return ans
    while len(str(n))>1:
        n,ans = ret(n,ans)
    return ans
    
def ret(n,ans):
    sum1=0
    for i in range(len(str(n))):
        sum1 += int(str(n)[i])
    ans += 1
    return sum1, ans
    
