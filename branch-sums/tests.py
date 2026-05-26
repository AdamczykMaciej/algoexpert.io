# Tests for Branch Sums
#
# Run with:   python -m unittest tests.py
#         or: python tests.py

import unittest

from main import BinaryTree, branchSums


def build(spec):
    """Build a BinaryTree from a nested (value, left_spec, right_spec) tuple.
    Pass None for missing children — keeps test setup explicit and easy to
    eyeball."""
    if spec is None:
        return None
    value, left, right = spec
    node = BinaryTree(value)
    node.left = build(left)
    node.right = build(right)
    return node


class TestBranchSums(unittest.TestCase):
    def test_sample_input(self):
        # The example from the problem statement.
        #         1
        #       /   \
        #      2     3
        #     / \   / \
        #    4   5 6   7
        #   / \  /
        #  8   9 10
        tree = build(
            (1,
                (2,
                    (4, (8, None, None), (9, None, None)),
                    (5, (10, None, None), None)),
                (3,
                    (6, None, None),
                    (7, None, None))),
        )
        self.assertEqual(branchSums(tree), [15, 16, 18, 10, 11])

    def test_single_node(self):
        # Root is also a leaf — single branch sum equal to its value.
        tree = build((42, None, None))
        self.assertEqual(branchSums(tree), [42])

    def test_left_skewed(self):
        # Only one branch (1 -> 2 -> 3 -> 4 down the left).
        tree = build(
            (1, (2, (3, (4, None, None), None), None), None),
        )
        self.assertEqual(branchSums(tree), [10])

    def test_right_skewed(self):
        # Only one branch, down the right.
        tree = build(
            (1, None, (2, None, (3, None, (4, None, None)))),
        )
        self.assertEqual(branchSums(tree), [10])

    def test_one_sided_children(self):
        # Mix of nodes with only-left and only-right children — guards on
        # individual children matter here.
        #       1
        #      /
        #     2
        #      \
        #       3
        #      /
        #     4
        tree = build(
            (1, (2, None, (3, (4, None, None), None)), None),
        )
        self.assertEqual(branchSums(tree), [10])

    def test_two_branches(self):
        # Simple V-shape — two leaves, two branch sums.
        #     1
        #    / \
        #   2   3
        tree = build((1, (2, None, None), (3, None, None)))
        self.assertEqual(branchSums(tree), [3, 4])

    def test_left_to_right_order(self):
        # Make sure branches come out left-to-right, not in some other order.
        #         5
        #       /   \
        #      1     9
        #     / \   / \
        #    2   3 4   6
        tree = build(
            (5,
                (1, (2, None, None), (3, None, None)),
                (9, (4, None, None), (6, None, None))),
        )
        # Branches: 5+1+2=8, 5+1+3=9, 5+9+4=18, 5+9+6=20
        self.assertEqual(branchSums(tree), [8, 9, 18, 20])

    def test_negative_values(self):
        # Negative and zero values — sums can cross zero mid-branch.
        #        -1
        #        / \
        #       2   -3
        #      /
        #     0
        tree = build(
            (-1, (2, (0, None, None), None), (-3, None, None)),
        )
        # Branches: -1+2+0 = 1, -1+-3 = -4
        self.assertEqual(branchSums(tree), [1, -4])

    def test_deep_unbalanced(self):
        # Multiple unbalanced branches of different lengths.
        #         1
        #       /   \
        #      2     3
        #     /       \
        #    4         5
        #   /           \
        #  6             7
        tree = build(
            (1,
                (2, (4, (6, None, None), None), None),
                (3, None, (5, None, (7, None, None)))),
        )
        # Branches: 1+2+4+6 = 13, 1+3+5+7 = 16
        self.assertEqual(branchSums(tree), [13, 16])


if __name__ == "__main__":
    unittest.main()
