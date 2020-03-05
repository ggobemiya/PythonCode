# Codesignal>Arcade>Intro #55 Problem
# This is not a good answer. But that's the answer I can give you now. 20/03/05
# When I finish all Arcade, I can give a good answer.

def differentSquares(matrix):
    if len(matrix)<2:
        return 0
    elif len(matrix[0]) < 2:
        return 0
    k=[]
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            k.append(str(matrix[i][j])+str(matrix[i][j+1])+str(matrix[i+1][j])+str(matrix[i+1][j+1]))
    
    return len(list(set(k)))            
