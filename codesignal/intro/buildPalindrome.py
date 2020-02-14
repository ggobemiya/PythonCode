# Codesignal>Arcade>Intro #45 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/14
# When I finish all Arcade, I can give a good answer.

def buildPalindrome(st):
    if st[::]==st[::-1]:
        return st
    else:
        ts = st[::-1]
        for i in range(len(st)):
            tsst = st+ts
            if tsst[::] == tsst[::-1]:
                ans = tsst
            ts = ts[1:]
        return ans
