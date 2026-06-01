# Depth-First Search
#
# Source: https://www.algoexpert.io/questions/depth-first-search
#
# You're given a Node class that has a name and an array of optional children
# nodes. When put together, nodes form an acyclic tree-like structure.
#
# Implement the depthFirstSearch method on the Node class, which takes in an
# empty array, traverses the tree using the Depth-First Search approach
# (specifically navigating the tree from left to right), stores all of the
# nodes' names in the input array, and returns it.
#
# Sample Input:
#               A
#           / | | \
#          B  C D  E
#         / \    / \
#        F   G  H  I
#           / \
#          J   K
#
# Sample Output:
#   ["A", "B", "F", "G", "J", "K", "C", "D", "H", "I", "E"]


# Solution: Recursive pre-order traversal
# Time: O(V + E) | Space: O(V)
#   V = number of nodes, E = number of edges
#
# At each node: record the name, then recurse into each child left-to-right.
# Pre-order ordering falls out of recording the current node before descending.
# Space is O(V) for the recursion stack in the worst case (a deeply unbalanced
# tree).

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)

        for c in self.children:
            c.depthFirstSearch(array)

        return array
