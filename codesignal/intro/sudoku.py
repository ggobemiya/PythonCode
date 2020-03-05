# Codesignal>Arcade>Intro #60 Problem
# This is not a good answer. But that's the answer I can give you now. 20/03/05
# When I finish all Arcade, I can give a good answer.

def sudoku(grid):
    a,b,c,d = [],[],[],[]
    for i in range(int(len(grid)/3)):
        for j in range(int(len(grid)/3)):
            a += grid[3*i+j][0:3]
            b += grid[3*i+j][3:6]
            c += grid[3*i+j][6:9]
            if len(set(grid[3*i+j])) !=9:
                return False
        if len(set(a)) != 9 or len(set(b))!= 9 or len(set(c)) != 9:
            return False
        else :
            a,b,c = [],[],[]
    for i in range(9):
        for j in range(9):
            d.append(grid[j][i])
        if len(set(d)) !=9:
            return False
        d = []
    return True


