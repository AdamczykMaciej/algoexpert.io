# Node Depths
#
# Source: https://www.algoexpert.io/questions/node-depths
#
# The distance between a node in a Binary Tree and the tree's root is called
# the node's depth.
#
# Write a function that takes in a Binary Tree and returns the sum of its
# nodes' depths.
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
#            / \
#           8   9
#
# Sample Output:
#   16
#   (depths: 0 + 1 + 1 + 2 + 2 + 2 + 2 + 3 + 3 = 16)


# Solution: Recursive sum with depth carried in the call
# Time: O(n) | Space: O(h)
#   n = number of nodes, h = tree height (O(log n) balanced, O(n) skewed)
#
# Visit every node once, passing each node's depth in as a recursion argument.
# At each node, return its own depth plus the sums returned by its subtrees.
# Base case (None) contributes 0. Total is the sum of every node's depth.
def func(node, totalDepth=0):
    if node is None:
        return 0

    return totalDepth + func(node.left, totalDepth + 1) + func(node.right, totalDepth + 1)


def nodeDepths(root):
    # Write your code here.
    return func(root, 0)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
