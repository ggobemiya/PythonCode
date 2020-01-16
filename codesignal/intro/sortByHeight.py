def sortByHeight(a):
    k = [[i,x] for i, x in enumerate(a) if x != -1]
    c = []
    d = []
    for i in range(len(k)):
        d.append(k[i][0])
        c.append(k[i][1])
    b = sorted(c)
    for i in range(len(d)):
        a[d[i]] = b[i]
    return a



# Codesignal>Arcade>Intro #12 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/16
# When I finish all Arcade, I can give a good answer.
