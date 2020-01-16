def isLucky(n):
    a=str(n)
    b=[]
    c=[]
    for i in range(len(a)//2):
        b.append(int(a[i]))
        c.append(int(a[i+len(a)//2]))
    return sum(b) == sum(c)

# Codesignal>Arcade>Intro #11 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/16
# When I finish all Arcade, I can give a good answer.
