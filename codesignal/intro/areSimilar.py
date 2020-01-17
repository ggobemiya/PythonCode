# Codesignal>Arcade>Intro #16 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/17
# When I finish all Arcade, I can give a good answer.

def areSimilar(a, b):
    if sorted(a)==sorted(b):
        ans = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                ans +=1
        if ans <=2 :
            return True
    return False
