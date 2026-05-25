# Tests for Transpose Matrix
#
# Run with:   python -m unittest tests.py
#         or: python tests.py
#
# Each test case is executed against both implementations in main.py via
# subTest, so a failure tells you exactly which solution broke.

import unittest

from main import (
    transposeMatrix,
    transposeMatrix_appended,
)

SOLUTIONS = [
    ("preallocated", transposeMatrix),
    ("appended", transposeMatrix_appended),
]


class TestTransposeMatrix(unittest.TestCase):
    def _run_all(self, matrix, expected):
        # Run the same case against every implementation. A deep copy of the
        # input is passed in so any in-place mutation can't leak between runs.
        for name, solution in SOLUTIONS:
            with self.subTest(solution=name):
                copy = [row[:] for row in matrix]
                self.assertEqual(solution(copy), expected)

    def test_sample_input(self):
        # The example from the problem statement: 3x2 -> 2x3.
        self._run_all(
            [[1, 2], [3, 4], [5, 6]],
            [[1, 3, 5], [2, 4, 6]],
        )

    def test_square_matrix(self):
        # Square matrix — transpose still has the same dimensions.
        self._run_all(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[1, 4, 7], [2, 5, 8], [3, 6, 9]],
        )

    def test_single_element(self):
        # 1x1 matrix is its own transpose.
        self._run_all([[7]], [[7]])

    def test_single_row(self):
        # 1xN row becomes an Nx1 column.
        self._run_all([[1, 2, 3, 4]], [[1], [2], [3], [4]])

    def test_single_column(self):
        # Nx1 column becomes a 1xN row.
        self._run_all([[1], [2], [3], [4]], [[1, 2, 3, 4]])

    def test_wide_rectangular(self):
        # 2x4 -> 4x2.
        self._run_all(
            [[1, 2, 3, 4], [5, 6, 7, 8]],
            [[1, 5], [2, 6], [3, 7], [4, 8]],
        )

    def test_tall_rectangular(self):
        # 4x2 -> 2x4.
        self._run_all(
            [[1, 2], [3, 4], [5, 6], [7, 8]],
            [[1, 3, 5, 7], [2, 4, 6, 8]],
        )

    def test_negative_values(self):
        # Negatives and zeros — sanity check that values pass through unchanged.
        self._run_all(
            [[-1, 0, 1], [2, -3, 4]],
            [[-1, 2], [0, -3], [1, 4]],
        )

    def test_does_not_mutate_input(self):
        # The transpose should not mutate the caller's matrix.
        original = [[1, 2], [3, 4]]
        snapshot = [row[:] for row in original]
        for _, solution in SOLUTIONS:
            with self.subTest(solution=solution.__name__):
                solution(original)
                self.assertEqual(original, snapshot)


if __name__ == "__main__":
    unittest.main()
