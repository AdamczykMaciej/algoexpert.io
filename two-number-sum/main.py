# Two Number Sum
#
# Source: https://www.algoexpert.io/questions/two-number-sum
#
# Write a function that takes in a non-empty array of distinct integers and an
# integer representing a target sum. If any two numbers in the input array sum
# up to the target sum, the function should return them in an array, in any
# order. If no two numbers sum up to the target sum, the function should return
# an empty array.
#
# Note that the target sum has to be obtained by summing two different integers
# in the array; you can't add a single integer to itself in order to obtain the
# target sum.
#
# You can assume that there will be at most one pair of numbers summing up to
# the target sum.
#
# Sample Input:
#   array = [3, 5, -4, 8, 11, 1, -1, 6]
#   targetSum = 10
#
# Sample Output:
#   [-1, 11] // the numbers could be in reverse order

# Solution 1: Brute force
# Time: O(n^2) | Space: O(1)
#
# Check every possible pair of numbers in the array. For each element, iterate
# through all elements after it (to avoid using the same index twice and to
# skip pairs we've already checked) and return the first pair that sums to the
# target. Simple but slow for large inputs.
def twoNumberSum_bruteforce(array, targetSum):
  for i in range(len(array)-1):
    for j in range(i+1, len(array)):
      if array[i]+array[j] == targetSum:
        return [array[i], array[j]]
  return []

# Solution 2: Hash table (one-pass)
# Time: O(n) | Space: O(n)
#
# For each number `num`, the complement we need is `targetSum - num`. As we
# walk through the array we keep a set of numbers we've already seen; if the
# complement is in that set, we've found our pair. Trades extra memory for a
# single linear pass — fastest of the three.
def twoNumberSum_hash(array, targetSum):
    nums = {} #hashtable, dict
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num]=True
    return []

# Solution 3: Sort + two pointers
# Time: O(n log n) | Space: O(1)
#
# Sort the array, then place one pointer at the start and one at the end.
# If the current sum is too small, move the left pointer right (increase the
# sum); if it's too big, move the right pointer left (decrease the sum). When
# they meet without finding a match, no pair exists. Uses no extra space
# beyond the sort, at the cost of an O(n log n) sort up front.
def twoNumberSum_twopointers(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1

    while left!=right:
        sum = array[left]+array[right]
        if sum == targetSum:
            return [array[left],array[right]]

        if sum < targetSum:
            left+=1
        elif sum > targetSum:
            right-=1

    return []
