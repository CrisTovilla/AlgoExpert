def transposeMatrix(matrix):
    # Write your code here.
    result = []
    for x in range(len(matrix)):
        row = []
        for y in range(len(matrix[x])):
            if y >= len(result):
                result.append([])
            result[y].append(matrix[x][y])
    return result
