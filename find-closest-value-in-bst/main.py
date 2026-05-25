# Find Closest Value in BST
#
# Source: https://www.algoexpert.io/questions/find-closest-value-in-bst
#
# Write a function that takes in a Binary Search Tree (BST) and a target
# integer value and returns the closest value to that target value contained
# in the BST.
#
# You can assume that there will only be one closest value.
#
# Each BST node has an integer value, a left child node, and a right child
# node. A node is said to be a valid BST node if and only if it satisfies the
# BST property: its value is strictly greater than the values of every node to
# its left; its value is less than or equal to the values of every node to its
# right; and its children nodes are either valid BST nodes themselves or None.
#
# Sample Input:
#                  10
#                /    \
#               5      15
#              / \    /  \
#             2   5  13   22
#            /        \
#           1         14
#   target = 12
#
# Sample Output:
#   13


# Solution: Iterative descent
# Time: O(log n) average, O(n) worst | Space: O(1)
#
# The BST property lets us prune half the tree at each step. Walk from the
# root: if the current node's value beats the best-so-far on |target - value|,
# update `closest`. Then go left if target < current, right if target > current,
# or return immediately on equality. Continue until we walk off the tree.
def findClosestValueInBst(tree, target):
    # Write your code here.
    node = tree
    closest = node.value
    while node is not None:
        diff = abs(target - node.value)
        if diff < abs(target - closest):
            closest = node.value
        # iterating
        if node.value > target:
            node = node.left
        elif node.value < target:
            node = node.right
        else:
            return node.value

    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
