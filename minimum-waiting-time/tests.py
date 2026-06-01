# Tests for Minimum Waiting Time
#
# Run with:   python -m unittest tests.py
#         or: python tests.py
#
# Each test case is executed against both implementations in main.py via
# subTest, so a failure tells you exactly which solution broke.

import unittest

from main import (
    minimumWaitingTime,
    minimumWaitingTime_nested,
)

SOLUTIONS = [
    ("nested", minimumWaitingTime_nested),
    ("linear", minimumWaitingTime),
]


class TestMinimumWaitingTime(unittest.TestCase):
    def _run_all(self, queries, expected):
        # Run the same case against every implementation. A copy of the input
        # is passed in since both solutions sort the array in place.
        for name, solution in SOLUTIONS:
            with self.subTest(solution=name):
                self.assertEqual(solution(list(queries)), expected)

    def test_sample_input(self):
        # Sorted [1, 2, 2, 3, 6] -> waits 0+1+3+5+8 = 17.
        self._run_all([3, 2, 1, 2, 6], 17)

    def test_problem_intro_example(self):
        # [1, 4, 5] sorted is itself -> waits 0 + 1 + 5 = 6.
        self._run_all([1, 4, 5], 6)

    def test_single_query(self):
        # One query waits for nothing.
        self._run_all([100], 0)

    def test_two_queries(self):
        # Smallest goes first -> shorter wait. Sorted [3, 5] -> waits 0+3 = 3.
        self._run_all([5, 3], 3)

    def test_already_sorted(self):
        # Sorted [1, 2, 3, 4] -> waits 0 + 1 + 3 + 6 = 10.
        self._run_all([1, 2, 3, 4], 10)

    def test_reverse_sorted(self):
        # Same multiset as above, different input order.
        self._run_all([4, 3, 2, 1], 10)

    def test_all_equal(self):
        # Five 7s. Sorted [7]*5 -> waits 0 + 7 + 14 + 21 + 28 = 70.
        self._run_all([7, 7, 7, 7, 7], 70)

    def test_with_duplicates(self):
        # Sorted [2, 2, 4, 4] -> waits 0 + 2 + 4 + 8 = 14.
        self._run_all([4, 2, 4, 2], 14)

    def test_does_not_depend_on_input_order(self):
        # Two different permutations of the same multiset must return the
        # same answer.
        a = [5, 1, 3, 8, 2]
        b = [8, 5, 3, 2, 1]
        results = [s(list(a)) for _, s in SOLUTIONS] + [
            s(list(b)) for _, s in SOLUTIONS
        ]
        self.assertEqual(len(set(results)), 1)


if __name__ == "__main__":
    unittest.main()
