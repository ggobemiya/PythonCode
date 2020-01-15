def matrixElementsSum(matrix):
    k = []
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] == 0:
                break
            k.append(matrix[i][j])
    return sum(k)
