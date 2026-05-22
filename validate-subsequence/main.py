# Validate Subsequence
#
# Source: https://www.algoexpert.io/questions/validate-subsequence
#
# Write a function that takes in two non-empty arrays of integers and returns
# a boolean representing whether the second array is a subsequence of the
# first one.
#
# A subsequence of an array is a set of numbers that aren't necessarily
# adjacent in the array but that are in the same order as they appear in the
# array. For instance, the numbers [1, 3, 4] form a subsequence of the array
# [1, 2, 3, 4], and so do the numbers [2, 4]. Note that a single number in an
# array and the array itself are both valid subsequences of the array.
#
# Sample Input:
#   array    = [5, 1, 22, 25, 6, -1, 8, 10]
#   sequence = [1, 6, -1, 10]
#
# Sample Output:
#   True


# Solution: Single pointer walk
# Time: O(n) | Space: O(1)
#
# Walk through `array` once, keeping a pointer `i` into `sequence`. Every time
# the current array element matches `sequence[i]`, advance `i`. If we manage
# to advance past the end of `sequence`, every element was found in order and
# the answer is True; otherwise we fall off the end of `array` first and
# return False. Order is preserved because we only ever move `i` forward.
def isValidSubsequence(array, sequence):
    # Write your code here.
    '''iterate over array.'''

    i=0
    for num in array:
        if i<len(sequence) and num == sequence[i]:
            i+=1
        if i==len(sequence):
            return True
    return False
