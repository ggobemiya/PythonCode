# Codesignal>Arcade>Intro #24 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/23
# When I finish all Arcade, I can give a good answer.


def minesweeper(matrix):
    true = True
    false = False
    a = len(matrix)
    b = len(matrix[0])
    for i in range(a):
        matrix[i].insert(b,"*")
        matrix[i].insert(0,"*")
    matrix.insert(0,[])
    matrix.insert(a+1,[])
    for i in range(len(matrix[1])):
        matrix[0].insert(i,"*")
        matrix[a+1].insert(i,"*")
    a = len(matrix)
    b = len(matrix[0])
    k = 0
    c1 = []
    c2 = []
    for i in range(1,a-1):
        for j in range(1,b-1):
            if matrix[i-1][j-1]==True:
                k +=1
            if matrix[i][j-1]==True:
                k +=1
            if matrix[i+1][j-1]==True:
                k +=1
            if matrix[i-1][j]==True:
                k +=1
            if matrix[i+1][j]==True:
                k +=1    
            if matrix[i-1][j+1]==True:
                k +=1
            if matrix[i][j+1]==True:
                k +=1
            if matrix[i+1][j+1]==True:
                k +=1
            c1.insert(j-1,k)
            k = 0
        c2.insert(i-1,c1)
        c1=[]
    return c2
