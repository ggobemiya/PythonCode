# Codesignal>Arcade>Intro #42 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/14
# When I finish all Arcade, I can give a good answer.

def bishopAndPawn(bishop, pawn):
    ans = False
    if ord(bishop[0])-ord(pawn[0]) == ord(bishop[1])-ord(pawn[1]):
        ans = True
    elif ord(bishop[0])+ord(bishop[1]) == ord(pawn[0])+ord(pawn[1]):
        ans = True
    return ans

