# Codesignal>Arcade>Intro #53 Problem
# This is not a good answer. But that's the answer I can give you now. 20/03/03
# When I finish all Arcade, I can give a good answer.

def validTime(time):
    ans = False
    if 0<=int(time[0:2])<24 and 0<=int(time[3:])<60:
        ans = True
    return ans
