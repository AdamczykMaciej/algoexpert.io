# Tests for Tournament Winner
#
# Run with:   python -m unittest tests.py
#         or: python tests.py

import unittest

from main import tournamentWinner


class TestTournamentWinner(unittest.TestCase):
    def test_sample_input(self):
        # The example from the problem statement.
        competitions = [
            ["HTML", "C#"],
            ["C#", "Python"],
            ["Python", "HTML"],
        ]
        results = [0, 0, 1]
        self.assertEqual(tournamentWinner(competitions, results), "Python")

    def test_home_team_sweeps(self):
        # Team A is always the home team and always wins — should take it
        # with 9 points (3 wins × 3).
        competitions = [
            ["A", "B"],
            ["A", "C"],
            ["A", "D"],
            ["B", "C"],
            ["B", "D"],
            ["C", "D"],
        ]
        results = [1, 1, 1, 1, 1, 1]
        self.assertEqual(tournamentWinner(competitions, results), "A")

    def test_away_team_sweeps(self):
        # All matches won by the away team — the team that's always the
        # away slot in its games should win.
        competitions = [
            ["A", "B"],
            ["A", "C"],
            ["B", "C"],
        ]
        results = [0, 0, 0]
        # B wins against A; C wins against A and B. So C is the winner.
        self.assertEqual(tournamentWinner(competitions, results), "C")

    def test_two_team_tournament(self):
        # Smallest possible tournament — only one match.
        competitions = [["Bulls", "Lakers"]]
        results = [1]
        self.assertEqual(tournamentWinner(competitions, results), "Bulls")

    def test_two_team_away_wins(self):
        # Mirror of the above — single match where the away team wins.
        competitions = [["Bulls", "Lakers"]]
        results = [0]
        self.assertEqual(tournamentWinner(competitions, results), "Lakers")

    def test_winner_announced_mid_tournament(self):
        # The eventual winner takes the lead early and then loses — make
        # sure we don't latch onto whoever was leading at any single point.
        competitions = [
            ["A", "B"],  # A wins -> A: 3
            ["A", "C"],  # C wins -> C: 3
            ["B", "C"],  # C wins -> C: 6
            ["B", "A"],  # B wins -> B: 3
        ]
        results = [1, 0, 0, 1]
        self.assertEqual(tournamentWinner(competitions, results), "C")

    def test_winner_emerges_late(self):
        # Winner has no points until the last few games but ends on top.
        competitions = [
            ["A", "B"],  # A wins -> A: 3
            ["A", "C"],  # A wins -> A: 6
            ["B", "C"],  # C wins -> C: 3
            ["C", "A"],  # C wins -> C: 6
            ["C", "B"],  # C wins -> C: 9
        ]
        results = [1, 1, 0, 1, 1]
        self.assertEqual(tournamentWinner(competitions, results), "C")

    def test_four_team_round_robin(self):
        # Full round-robin with four teams (6 matches). Designed so D wins
        # cleanly with 9 points.
        competitions = [
            ["A", "B"],  # B
            ["A", "C"],  # C
            ["A", "D"],  # D
            ["B", "C"],  # C
            ["B", "D"],  # D
            ["C", "D"],  # D
        ]
        results = [0, 0, 0, 0, 0, 0]
        # Points: A=0, B=3, C=6, D=9 -> D wins.
        self.assertEqual(tournamentWinner(competitions, results), "D")


if __name__ == "__main__":
    unittest.main()
