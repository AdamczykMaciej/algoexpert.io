# Tests for Find Closest Value in BST
#
# Run with:   python -m unittest tests.py
#         or: python tests.py

import unittest

from main import BST, findClosestValueInBst


def insert(root, value):
    """Insert `value` into a BST rooted at `root`, returning the (possibly new)
    root. Used to keep test setup terse."""
    if root is None:
        return BST(value)
    node = root
    while True:
        if value < node.value:
            if node.left is None:
                node.left = BST(value)
                return root
            node = node.left
        else:
            if node.right is None:
                node.right = BST(value)
                return root
            node = node.right


def build(values):
    """Build a BST by inserting `values` in order. The resulting shape depends
    on the insertion order, which matches how the problem statement draws its
    sample trees."""
    root = None
    for v in values:
        root = insert(root, v)
    return root


# The canonical sample tree from the problem statement:
#
#                  10
#                /    \
#               5      15
#              / \    /  \
#             2   5  13   22
#            /        \
#           1         14
SAMPLE_VALUES = [10, 5, 15, 2, 5, 13, 22, 1, 14]


class TestFindClosestValueInBst(unittest.TestCase):
    def test_sample_input(self):
        # The example from the problem statement.
        tree = build(SAMPLE_VALUES)
        self.assertEqual(findClosestValueInBst(tree, 12), 13)

    def test_exact_match_root(self):
        # Target equals the root value — exact match should win.
        tree = build(SAMPLE_VALUES)
        self.assertEqual(findClosestValueInBst(tree, 10), 10)

    def test_exact_match_leaf(self):
        # Target equals a leaf value — exact match wins regardless of depth.
        tree = build(SAMPLE_VALUES)
        self.assertEqual(findClosestValueInBst(tree, 14), 14)

    def test_target_below_min(self):
        # Target smaller than every value — answer is the minimum (1).
        tree = build(SAMPLE_VALUES)
        self.assertEqual(findClosestValueInBst(tree, -100), 1)

    def test_target_above_max(self):
        # Target larger than every value — answer is the maximum (22).
        tree = build(SAMPLE_VALUES)
        self.assertEqual(findClosestValueInBst(tree, 100), 22)

    def test_target_between_two_nodes(self):
        # Target = 4, closer to 5 than to 2.
        tree = build(SAMPLE_VALUES)
        self.assertEqual(findClosestValueInBst(tree, 4), 5)

    def test_target_just_below_node(self):
        # Target = 13, exact match — should find it directly.
        tree = build(SAMPLE_VALUES)
        self.assertEqual(findClosestValueInBst(tree, 13), 13)

    def test_single_node_tree(self):
        # Tree with only a root — closest is always the root's value.
        tree = BST(42)
        self.assertEqual(findClosestValueInBst(tree, 0), 42)
        self.assertEqual(findClosestValueInBst(tree, 42), 42)
        self.assertEqual(findClosestValueInBst(tree, 1000), 42)

    def test_skewed_right(self):
        # All values inserted in ascending order — degenerates to a right
        # spine. Walking should still find the closest.
        tree = build([1, 2, 3, 4, 5])
        self.assertEqual(findClosestValueInBst(tree, 4), 4)
        self.assertEqual(findClosestValueInBst(tree, 10), 5)

    def test_skewed_left(self):
        # Descending insertion order — left spine.
        tree = build([5, 4, 3, 2, 1])
        self.assertEqual(findClosestValueInBst(tree, 2), 2)
        self.assertEqual(findClosestValueInBst(tree, -10), 1)

    def test_negative_values(self):
        # Tree with negative values — sanity check on signed arithmetic.
        tree = build([-10, -20, -5, -15, -1])
        self.assertEqual(findClosestValueInBst(tree, -16), -15)
        self.assertEqual(findClosestValueInBst(tree, 0), -1)


if __name__ == "__main__":
    unittest.main()
