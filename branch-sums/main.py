# Branch Sums
#
# Source: https://www.algoexpert.io/questions/branch-sums
#
# Write a function that takes in a Binary Tree and returns a list of its
# branch sums ordered from leftmost branch sum to rightmost branch sum.
#
# A branch sum is the sum of all values in a Binary Tree branch. A Binary
# Tree branch is a path of nodes in a tree that starts at the root node and
# ends at any leaf node.
#
# Each BinaryTree node has an integer value, a left child node, and a right
# child node. Children nodes can either be BinaryTree nodes themselves or None.
#
# Sample Input:
#                  1
#                /   \
#               2     3
#              / \   / \
#             4   5 6   7
#            / \  /
#           8   9 10
#
# Sample Output:
#   [15, 16, 18, 10, 11]
#   (1+2+4+8, 1+2+4+9, 1+2+5+10, 1+3+6, 1+3+7)


# Solution: DFS with running accumulator
# Time: O(n) | Space: O(n)
#
# Walk the tree depth-first carrying a running sum from the root. When we
# reach a leaf (both children None), record the current path total. Children
# are visited left-before-right so the output preserves left-to-right branch
# order. Space is O(n) — call stack up to the tree's height (O(n) for a
# skewed tree) plus the result list.
def _collectSums(node, runningSum, results):
    newSum = runningSum + node.value

    if node.left is None and node.right is None:
        results.append(newSum)
        return

    if node.left is not None:
        _collectSums(node.left, newSum, results)
    if node.right is not None:
        _collectSums(node.right, newSum, results)


def branchSums(root):
    # Write your code here.
    results = []
    _collectSums(root, 0, results)
    return results


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
