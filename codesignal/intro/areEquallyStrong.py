# Codesignal>Arcade>Intro #19 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/20
# When I finish all Arcade, I can give a good answer.

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    a = [yourLeft, yourRight, friendsLeft, friendsRight]
    ans = False
    if a[0] is a[2] and a[1] is a[3]:
        ans = True
    if a[0] is a[3] and a[1] is a[2]:
        ans = True
    return ans
