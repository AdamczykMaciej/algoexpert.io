# Tests for Class Photos
#
# Run with:   python -m unittest tests.py
#         or: python tests.py
#
# Each test case runs against all three implementations via subTest so a
# failure points at the specific solution that broke.

import unittest

from main import (
    classPhotos,
    classPhotos_canonical,
    classPhotos_flag,
)

SOLUTIONS = [
    ("flag", classPhotos_flag),
    ("canonical", classPhotos_canonical),
    ("zip", classPhotos),
]


class TestClassPhotos(unittest.TestCase):
    def _run_all(self, red, blue, expected):
        # Run the same case against every implementation. Both inputs are
        # copied since all solutions sort in place.
        for name, solution in SOLUTIONS:
            with self.subTest(solution=name):
                self.assertEqual(solution(list(red), list(blue)), expected)

    def test_sample_input(self):
        # The example from the problem statement.
        self._run_all([5, 8, 1, 3, 4], [6, 9, 2, 4, 5], True)

    def test_red_dominates(self):
        # Red is taller everywhere -> red in back is fine.
        self._run_all([6, 9, 2, 4, 5], [5, 8, 1, 3, 4], True)

    def test_equal_at_tallest(self):
        # Tallest pair is equal -> no strict-taller back row possible.
        self._run_all([5, 8, 1, 3, 4], [5, 8, 1, 3, 4], False)

    def test_interleaved_heights(self):
        # After sorting the two rows leapfrog each other -> no valid back row.
        # Sorted: red=[1,3,5], blue=[2,4,6]. Blue back works? blue must be > red
        # at every index: 6>5, 4>3, 2>1 -> yes. So this should return True.
        self._run_all([1, 3, 5], [2, 4, 6], True)

    def test_one_violation_in_middle(self):
        # Sorted asc: red=[1,5,8], blue=[2,4,10]. Try blue back: 10>8 ✓,
        # 4>5 ✗ -> fail. Try red back: 8>10 ✗ -> fail. Expect False.
        self._run_all([1, 5, 8], [2, 4, 10], False)

    def test_single_pair_strict(self):
        # Smallest possible input — one pair, strict inequality.
        self._run_all([3], [4], True)

    def test_single_pair_equal(self):
        # One pair, equal -> False (not strictly taller).
        self._run_all([3], [3], False)

    def test_red_all_taller(self):
        # Disjoint ranges — red strictly taller everywhere.
        self._run_all([10, 11, 12], [1, 2, 3], True)

    def test_does_not_change_answer_with_input_order(self):
        # Two different input orderings of the same multisets must agree.
        red_a = [5, 8, 1, 3, 4]
        blue_a = [6, 9, 2, 4, 5]
        red_b = list(reversed(red_a))
        blue_b = list(reversed(blue_a))
        results = []
        for _, solution in SOLUTIONS:
            results.append(solution(list(red_a), list(blue_a)))
            results.append(solution(list(red_b), list(blue_b)))
        self.assertEqual(len(set(results)), 1)


if __name__ == "__main__":
    unittest.main()
