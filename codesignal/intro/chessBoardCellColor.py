# Codesignal>Arcade>Intro #29 Problem
# This is not a good answer. But that's the answer I can give you now. 20/02/05
# When I finish all Arcade, I can give a good answer.


def chessBoardCellColor(cell1, cell2):
    return (ord(cell1[0])+ord(cell1[1]))%2 == (ord(cell2[0])+ord(cell2[1]))%2
