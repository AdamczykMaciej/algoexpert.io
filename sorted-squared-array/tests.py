# Tests for Sorted Squared Array
#
# Run with:   python -m unittest tests.py
#         or: python tests.py
#
# Each test case is executed against both implementations in main.py via
# subTest, so a failure tells you exactly which solution broke.

import unittest

from main import (
    sortedSquaredArray,
    sortedSquaredArray_sort,
)

SOLUTIONS = [
    ("sort", sortedSquaredArray_sort),
    ("twopointers", sortedSquaredArray),
]


class TestSortedSquaredArray(unittest.TestCase):
    def _run_all(self, array, expected):
        # Run the same case against every implementation. A copy of the input
        # is passed in so any in-place mutation doesn't leak between runs.
        for name, solution in SOLUTIONS:
            with self.subTest(solution=name):
                self.assertEqual(solution(list(array)), expected)

    def test_sample_input(self):
        # The example from the problem statement.
        self._run_all([1, 2, 3, 5, 6, 8, 9], [1, 4, 9, 25, 36, 64, 81])

    def test_all_positive(self):
        # Already-sorted squares — output equals squaring each element.
        self._run_all([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])

    def test_all_negative(self):
        # All negatives: squaring reverses the order.
        self._run_all([-5, -4, -3, -2, -1], [1, 4, 9, 16, 25])

    def test_mixed_signs(self):
        # Negatives and positives interleave after squaring — the classic
        # case the two-pointer solution is designed for.
        self._run_all([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100])

    def test_contains_zero(self):
        # Zero should land wherever it sorts naturally.
        self._run_all([-3, -2, 0, 2, 3], [0, 4, 4, 9, 9])

    def test_single_element_positive(self):
        # Smallest valid input — single positive.
        self._run_all([5], [25])

    def test_single_element_negative(self):
        # Smallest valid input — single negative.
        self._run_all([-5], [25])

    def test_single_element_zero(self):
        # Single zero — square is still zero.
        self._run_all([0], [0])

    def test_two_elements(self):
        # Two-element input with mixed signs.
        self._run_all([-2, 3], [4, 9])

    def test_duplicates(self):
        # Repeated values (allowed since the input is "sorted ascending",
        # not strictly increasing).
        self._run_all([-2, -2, 0, 2, 2], [0, 4, 4, 4, 4])

    def test_large_negative_dominates(self):
        # Most-negative element has the largest absolute value, so its
        # square belongs at the end of the output.
        self._run_all([-10, -5, 0, 1, 2], [0, 1, 4, 25, 100])


if __name__ == "__main__":
    unittest.main()
