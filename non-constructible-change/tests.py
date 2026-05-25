# Tests for Non-Constructible Change
#
# Run with:   python -m unittest tests.py
#         or: python tests.py

import unittest

from main import nonConstructibleChange


class TestNonConstructibleChange(unittest.TestCase):
    def test_sample_input(self):
        # The example from the problem statement.
        self.assertEqual(
            nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]), 20
        )

    def test_empty(self):
        # No coins — the smallest unmakeable amount is 1.
        self.assertEqual(nonConstructibleChange([]), 1)

    def test_single_one(self):
        # One coin worth 1 — we can make 1 but not 2.
        self.assertEqual(nonConstructibleChange([1]), 2)

    def test_single_large(self):
        # Single coin larger than 1 — we can't even make 1.
        self.assertEqual(nonConstructibleChange([5]), 1)

    def test_no_one_coin(self):
        # No coin of value 1 — answer is 1 regardless of other coins.
        self.assertEqual(nonConstructibleChange([2, 4, 6]), 1)

    def test_problem_intro_example(self):
        # The [1, 2, 5] example from the problem description.
        self.assertEqual(nonConstructibleChange([1, 2, 5]), 4)

    def test_all_ones(self):
        # k ones can make 1..k, so the answer is k + 1.
        self.assertEqual(nonConstructibleChange([1, 1, 1, 1]), 5)

    def test_consecutive_integers(self):
        # 1..5 covers everything up to 15; 16 is the first gap.
        self.assertEqual(nonConstructibleChange([1, 2, 3, 4, 5]), 16)

    def test_gap_at_start(self):
        # Reachable set after [1, 1, 2] is 1..4. A coin worth 6 leaves 5
        # unreachable.
        self.assertEqual(nonConstructibleChange([1, 1, 2, 6]), 5)

    def test_duplicates_at_boundary(self):
        # Duplicate coins extending reachability — [1, 1, 1, 1, 1, 7]
        # covers 1..5 with the ones, then 7 leaves 6 as the gap.
        self.assertEqual(
            nonConstructibleChange([1, 1, 1, 1, 1, 7]), 6
        )

    def test_unsorted_input(self):
        # Solution must sort internally — verify it doesn't depend on input order.
        self.assertEqual(
            nonConstructibleChange([7, 1, 5, 2, 1, 3]), 20
        )


if __name__ == "__main__":
    unittest.main()
