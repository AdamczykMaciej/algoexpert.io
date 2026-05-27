# Tests for Node Depths
#
# Run with:   python -m unittest tests.py
#         or: python tests.py

import unittest

from main import BinaryTree, nodeDepths


def build(spec):
    """Build a BinaryTree from a nested (value, left_spec, right_spec) tuple.
    Pass None for missing children."""
    if spec is None:
        return None
    value, left, right = spec
    node = BinaryTree(value)
    node.left = build(left)
    node.right = build(right)
    return node


class TestNodeDepths(unittest.TestCase):
    def test_sample_input(self):
        # The example from the problem statement.
        #         1
        #       /   \
        #      2     3
        #     / \   / \
        #    4   5 6   7
        #   / \
        #  8   9
        tree = build(
            (1,
                (2,
                    (4, (8, None, None), (9, None, None)),
                    (5, None, None)),
                (3,
                    (6, None, None),
                    (7, None, None))),
        )
        # Depths: 0 + 1 + 1 + 2 + 2 + 2 + 2 + 3 + 3 = 16
        self.assertEqual(nodeDepths(tree), 16)

    def test_single_node(self):
        # Just the root — depth 0, sum 0.
        tree = build((1, None, None))
        self.assertEqual(nodeDepths(tree), 0)

    def test_two_nodes_left(self):
        # Root + one left child — sum = 0 + 1.
        tree = build((1, (2, None, None), None))
        self.assertEqual(nodeDepths(tree), 1)

    def test_two_nodes_right(self):
        # Root + one right child — sum = 0 + 1.
        tree = build((1, None, (2, None, None)))
        self.assertEqual(nodeDepths(tree), 1)

    def test_balanced_three_levels(self):
        # Full balanced tree of height 2: 1 root + 2 children + 4 grandchildren.
        # Depths: 0, 1, 1, 2, 2, 2, 2 -> sum = 10.
        tree = build(
            (1,
                (2, (4, None, None), (5, None, None)),
                (3, (6, None, None), (7, None, None))),
        )
        self.assertEqual(nodeDepths(tree), 10)

    def test_left_skewed(self):
        # All left children — depths 0..n-1, sum = n*(n-1)/2.
        tree = build(
            (1, (2, (3, (4, (5, None, None), None), None), None), None),
        )
        # Depths: 0 + 1 + 2 + 3 + 4 = 10
        self.assertEqual(nodeDepths(tree), 10)

    def test_right_skewed(self):
        # Mirror of the left-skewed case.
        tree = build(
            (1, None, (2, None, (3, None, (4, None, (5, None, None))))),
        )
        self.assertEqual(nodeDepths(tree), 10)

    def test_negative_node_values(self):
        # Node values don't affect the sum — only the tree shape does. Sanity
        # check that the algorithm doesn't accidentally use node.value.
        tree = build(
            (-1, (-2, (-3, None, None), None), (-4, None, None)),
        )
        # Depths: 0 + 1 + 2 + 1 = 4
        self.assertEqual(nodeDepths(tree), 4)


if __name__ == "__main__":
    unittest.main()
