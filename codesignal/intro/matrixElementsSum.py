def matrixElementsSum(matrix):
    k = []
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] == 0:
                break
            k.append(matrix[i][j])
    return sum(k)


# Codesignal>Arcade>Intro #8 Problem
# This is not a good answer. But that's the answer I can give you now. 20/01/15
# When I finish all Arcade, I can give a good answer.
