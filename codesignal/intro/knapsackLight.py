# Codesignal>Arcade>Intro #39 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/14
# When I finish all Arcade, I can give a good answer.

def knapsackLight(value1, weight1, value2, weight2, maxW):
    a = [[value1,weight1],[value2,weight2]]
    b = []
    if maxW >= weight1 + weight2:
        return value1 + value2
    elif maxW < weight1 and maxW < weight2:
        return 0
    else:
        for i in [0,1]:
            if a[i][1]<=maxW:
                b.append(a[i])
        if len(b) ==2:
            return max(b[0][0],b[1][0])
        else:
            return b[0][0]
