# Codesignal>Arcade>Intro #58 Problem
# This is not a good answer. But that's the answer I can give you now. 20/03/05
# When I finish all Arcade, I can give a good answer.

def messageFromBinaryCode(code):
    ans = ""
    for i in range(int(len(code)/8)):
        ans += chr(int(code[8*(i):8*(i+1)],base=2))
    return ans
