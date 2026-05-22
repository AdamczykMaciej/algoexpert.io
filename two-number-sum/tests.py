# Tests for Two Number Sum
#
# Run with:   python -m unittest tests.py
#         or: python tests.py
#
# Each test case is executed against all three implementations in main.py via
# subTest, so a failure tells you exactly which solution broke.

import unittest

from main import (
    twoNumberSum_bruteforce,
    twoNumberSum_hash,
    twoNumberSum_twopointers,
)

SOLUTIONS = [
    ("bruteforce", twoNumberSum_bruteforce),
    ("hash", twoNumberSum_hash),
    ("twopointers", twoNumberSum_twopointers),
]


class TestTwoNumberSum(unittest.TestCase):
    def _run_all(self, array, targetSum, expected):
        # Run the same case against every implementation. A copy of the input
        # is passed in so the two-pointer solution's in-place sort doesn't
        # leak between runs.
        for name, solution in SOLUTIONS:
            with self.subTest(solution=name):
                result = solution(list(array), targetSum)
                if expected == []:
                    self.assertEqual(result, [])
                else:
                    # Pair may be returned in either order.
                    self.assertEqual(sorted(result), sorted(expected))

    def test_sample_input(self):
        # The example given in the problem statement.
        self._run_all([3, 5, -4, 8, 11, 1, -1, 6], 10, [-1, 11])

    def test_pair_at_start(self):
        # Matching pair is at the very beginning of the array.
        self._run_all([1, 2, 3, 4, 5], 3, [1, 2])

    def test_pair_at_end(self):
        # Matching pair is at the very end of the array.
        self._run_all([1, 2, 3, 4, 5], 9, [4, 5])

    def test_negative_numbers(self):
        # Target is reached using two negative numbers. Input chosen so only
        # one pair sums to -12 (the problem guarantees at most one match).
        self._run_all([-7, -5, -3, -1], -12, [-7, -5])

    def test_mixed_signs(self):
        # Pair spanning negative and positive values. Target 4 only matches
        # (-3, 7); no other pair in this array sums to 4.
        self._run_all([-3, -1, 2, 4, 7], 4, [-3, 7])

    def test_no_match(self):
        # No two numbers sum to the target — expect empty array.
        self._run_all([1, 2, 3, 4, 5], 100, [])

    def test_two_element_array_match(self):
        # Smallest possible matching input.
        self._run_all([4, 6], 10, [4, 6])

    def test_two_element_array_no_match(self):
        # Smallest possible non-matching input.
        self._run_all([4, 6], 11, [])

    def test_cannot_reuse_same_element(self):
        # 5 + 5 == 10, but the problem says you can't use the same element
        # twice and the array has distinct integers, so this must return [].
        self._run_all([5, 1, 2, 3], 10, [])


if __name__ == "__main__":
    unittest.main()
