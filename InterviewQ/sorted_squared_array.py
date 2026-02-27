def sortedSquaredArray(array):
    # Write your code here.
    leftI = 0
    rightI = len(array) - 1
    sortedSquares = [0 for _ in array]

    for index in reversed(range(len(array))):
        leftN =  array[leftI]
        rightN = array[rightI]

        if abs(leftN) > abs(rightN):
            sortedSquares[index] = leftN**2
            leftI = leftI + 1
        else:
            sortedSquares[index] = rightN**2
            rightI = rightI - 1
    
    return sortedSquares
