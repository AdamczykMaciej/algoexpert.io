# Non-Constructible Change
#
# Source: https://www.algoexpert.io/questions/non-constructible-change
#
# Given an array of positive integers representing the values of coins in your
# possession, write a function that returns the minimum amount of change (the
# minimum sum of money) that you cannot create. The given coins can have any
# positive integer value and aren't necessarily unique (i.e., you can have
# multiple coins of the same value).
#
# For example, if you're given coins = [1, 2, 5], the minimum amount of change
# that you can't create is 4. If you're given no coins, the minimum amount of
# change that you can't create is 1.
#
# Sample Input:
#   coins = [5, 7, 1, 1, 2, 3, 22]
#
# Sample Output:
#   20


# Solution: Sort + running reachable maximum
# Time: O(n log n) | Space: O(1)
#
# Sort the coins ascending. Walk through them keeping `currentChange` — the
# largest amount we can make using the coins seen so far. Invariant: every
# amount from 1..currentChange is reachable.
#
# When we look at the next coin c:
#   - If c > currentChange + 1, the value currentChange + 1 can never be made
#     (no remaining coin is small enough to fill the gap), so it's the answer.
#   - Otherwise, adding c extends our reachable range to currentChange + c.
#
# If we exhaust the coins without finding a gap, the answer is currentChange + 1.
def nonConstructibleChange(coins):

    '''
    [5,7,1,1,2,3,22]
    [1,1,2,3,5,7,22]

    1 -> 1
    1,1 -> 1,2
    1,1,2 -> 1,2,3,4
    1,1,2,3 -> 1,2,3,4,5,6,7
    1,1,2,3,5 -> 1,2,3,4,5,6,7,8,9,10,11,12
    '''
    coins.sort()


    currentChange = 0
    for c in coins:
        if c > currentChange + 1:
            return currentChange + 1
        currentChange += c

    return currentChange + 1
