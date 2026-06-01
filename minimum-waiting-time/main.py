# Minimum Waiting Time
#
# Source: https://www.algoexpert.io/questions/minimum-waiting-time
#
# You're given a non-empty array of positive integers representing the
# amounts of time that specific queries take to execute. Only one query can
# be executed at a time, but the queries can be executed in any order.
#
# A query's "waiting time" is defined as the amount of time that it must wait
# before its execution starts. In other words, if a query is executed second,
# then its waiting time is the duration of the first query; if a query is
# executed third, then its waiting time is the sum of the durations of the
# first two queries.
#
# Write a function that returns the minimum amount of total waiting time for
# all of the queries. For example, if you're given the queries of durations
# [1, 4, 5], then the minimum total waiting time is 5 (1 waits 0, 4 waits 1,
# 5 waits 1+4=5; total waited = 0+1+5 = 6 in the order [1,4,5]).
#
# Note: you're allowed to mutate the input array.
#
# Sample Input:
#   queries = [3, 2, 1, 2, 6]
#
# Sample Output:
#   17
#   (sorted: [1, 2, 2, 3, 6] -> waits 0 + 1 + 3 + 5 + 8 = 17)


# Solution 1: Sort + nested sum
# Time: O(n^2) | Space: O(1)
#
# Sort ascending (shortest first minimizes total waiting time — a longer query
# delays everyone behind it more than a shorter one would). Then for each
# query at position i, add up the durations of all queries before it.
# Correct but does the same prefix work over and over.
def minimumWaitingTime_nested(queries):
    queries.sort()
    sum = 0
    for i in range(1, len(queries)):
        for j in range(i):
            sum += queries[j]
    return sum


# Solution 2: Sort + multiplicative contribution
# Time: O(n log n) | Space: O(1)
#
# Same sort, but observe each query's contribution directly. The j-th query
# (0-indexed, after sorting) sits in front of (n - 1 - j) later queries, so
# it adds queries[j] to each of their waiting times — a total contribution
# of queries[j] * (n - 1 - j). Sum that over all j in one pass; the sort
# now dominates the runtime.
def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    n = len(queries)
    total = 0
    for j, q in enumerate(queries):
        total += q * (n - 1 - j)
    return total
