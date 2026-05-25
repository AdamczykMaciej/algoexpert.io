# Transpose Matrix
#
# Source: https://www.algoexpert.io/questions/transpose-matrix
#
# You're given a 2D array of integers matrix. Write a function that returns
# the transpose of the matrix.
#
# The transpose of a matrix is a flipped version of the original matrix across
# its main diagonal (which runs from the top-left to the bottom-right); it
# switches the row and column indices of the original matrix.
#
# You can assume the input matrix always has at least 1 value; however its
# width and height are not necessarily the same.
#
# Sample Input:
#   matrix = [
#       [1, 2],
#       [3, 4],
#       [5, 6],
#   ]
#
# Sample Output:
#   [
#       [1, 3, 5],
#       [2, 4, 6],
#   ]


# Solution 1: Preallocate the result, fill by index
# Time: O(w * h) | Space: O(w * h)
#
# Allocate the result as an w-by-h grid up front (where the input is h-by-w),
# then copy each element to its swapped position. Index swap: result[c][r] = matrix[r][c].
def transposeMatrix(matrix):
    # Write your code here.
    newMatrix = [[None for _ in matrix] for _ in matrix[0]]
    for rix, r in enumerate(matrix):
        for cix, c in enumerate(r):
            newMatrix[cix][rix] = matrix[rix][cix]
    return newMatrix


# Solution 2: Build row-by-row
# Time: O(w * h) | Space: O(w * h)
#
# Same complexity, different shape: iterate columns of the input as the outer
# loop, collect each column into a new row, append to the result. Avoids the
# preallocation step.
def transposeMatrix_appended(matrix):
    # Write your code here.
    newMatrix = []
    for cix in range(len(matrix[0])):
        newRow = []
        for rix in range(len(matrix)):
            newRow.append(matrix[rix][cix])
        newMatrix.append(newRow)
    return newMatrix
