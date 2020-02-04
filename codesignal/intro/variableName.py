# Codesignal>Arcade>Intro #27 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/04
# When I finish all Arcade, I can give a good answer.

def variableName(name):
    ans = True
    if name[0].isdigit():
        return False
    for i in range(len(name)):
        ans = name[i].isalnum() or name[i]=="_"
        if ans == False:
            break
    return ans

