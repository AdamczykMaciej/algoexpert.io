# Sorted Squared Array
#
# Source: https://www.algoexpert.io/questions/sorted-squared-array
#
# Write a function that takes in a non-empty array of integers that are sorted
# in ascending order and returns a new array of the same length with the
# squares of the original integers also sorted in ascending order.
#
# Sample Input:
#   array = [1, 2, 3, 5, 6, 8, 9]
#
# Sample Output:
#   [1, 4, 9, 25, 36, 64, 81]


# Solution 1: Square then sort
# Time: O(n log n) | Space: O(n)
#
# Square every element, then sort. Simple and short, but throws away the fact
# that the input is already sorted — the sort is the bottleneck.
def sortedSquaredArray_sort(array):
    # Write your code here.
    lst = list(map(lambda x: x**2, array))
    lst.sort()
    return lst


# Solution 2: Two pointers, fill from the back
# Time: O(n) | Space: O(n)
#
# The input is sorted, so the largest square must come from either the most
# negative or the most positive element. Keep one pointer at each end and
# write into the result array from the back: at each step, take whichever
# end has the larger absolute value, square it, and advance that pointer
# inward. After n steps every slot is filled in descending order from the
# back, which is ascending order from the front.
def sortedSquaredArray(array):
    # Write your code here.
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue ** 2
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue ** 2
            largerValueIdx -= 1
    return sortedSquares
