def matrixElementsSum(matrix):

    numrows = len(matrix)
    numcols = len(matrix[0])
    matrix_sum = []

    for i in range(numcols):
        for j in range(numrows):

            x = matrix[j][i]
            if x == 0:
                break
            else:
                matrix_sum.append(x)

    return sum(matrix_sum)

result = matrixElementsSum( [[0,1,1,2], [0,5,0,0], [2,0,3,3]])
print(result)
