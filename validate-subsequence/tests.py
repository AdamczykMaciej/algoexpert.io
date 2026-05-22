# Tests for Validate Subsequence
#
# Run with:   python -m unittest tests.py
#         or: python tests.py

import unittest

from main import isValidSubsequence


class TestIsValidSubsequence(unittest.TestCase):
    def test_sample_input(self):
        # The example from the problem statement.
        self.assertTrue(
            isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
        )

    def test_sequence_equals_array(self):
        # The full array is always a valid subsequence of itself.
        self.assertTrue(isValidSubsequence([1, 2, 3, 4], [1, 2, 3, 4]))

    def test_single_element_present(self):
        # A single matching element is a valid subsequence.
        self.assertTrue(isValidSubsequence([1, 2, 3, 4], [3]))

    def test_single_element_absent(self):
        # A single element not in the array is not a subsequence.
        self.assertFalse(isValidSubsequence([1, 2, 3, 4], [5]))

    def test_wrong_order(self):
        # Elements exist in the array but in the wrong order.
        self.assertFalse(isValidSubsequence([1, 2, 3, 4], [3, 1]))

    def test_sequence_longer_than_array(self):
        # A sequence longer than the array cannot be a subsequence.
        self.assertFalse(isValidSubsequence([1, 2], [1, 2, 3]))

    def test_missing_element(self):
        # First two elements match but the third is missing.
        self.assertFalse(isValidSubsequence([1, 2, 3, 4], [1, 2, 5]))

    def test_subsequence_at_end(self):
        # Subsequence appears at the tail of the array.
        self.assertTrue(isValidSubsequence([1, 2, 3, 4, 5], [4, 5]))

    def test_subsequence_at_start(self):
        # Subsequence appears at the head of the array.
        self.assertTrue(isValidSubsequence([1, 2, 3, 4, 5], [1, 2]))

    def test_non_adjacent_matches(self):
        # Matches are spread out — subsequences need not be contiguous.
        self.assertTrue(isValidSubsequence([1, 9, 2, 9, 3], [1, 2, 3]))

    def test_repeated_values_in_sequence(self):
        # A repeated value in the sequence must match two separate positions
        # in the array (i.e. the pointer only advances on each match).
        self.assertTrue(isValidSubsequence([1, 1, 2, 3], [1, 1, 3]))

    def test_repeated_value_only_appears_once_in_array(self):
        # Sequence needs the value twice but the array only has it once.
        self.assertFalse(isValidSubsequence([1, 2, 3], [1, 1]))


if __name__ == "__main__":
    unittest.main()
