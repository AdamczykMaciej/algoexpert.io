# Tournament Winner
#
# Source: https://www.algoexpert.io/questions/tournament-winner
#
# There's an algorithms tournament taking place in which teams of programmers
# compete against each other to solve algorithmic problems as fast as possible.
# Teams compete in a round-robin, where each team faces off against all other
# teams. Only two teams compete against each other at a time, and for each
# competition, one team is designated the home team while the other team is
# the away team. In each competition there's always one winner and one loser;
# there are no ties. A team receives 3 points if it wins and 0 points if it
# loses. The winner of the tournament is the team that receives the most total
# points.
#
# Given an array of pairs representing the teams that have competed against
# each other and an array containing the results of each competition, write
# a function that returns the winner of the tournament. The input arrays are
# never empty, and they have the same length. Each result in `results` denotes
# the winner of the corresponding competition: a result of 1 means the home
# team won; a result of 0 means the away team won.
#
# It's guaranteed that exactly one team will win the tournament and that each
# team will compete against all other teams exactly once. It's also guaranteed
# that the tournament will always have at least two teams.
#
# Sample Input:
#   competitions = [
#       ["HTML",   "C#"],
#       ["C#",     "Python"],
#       ["Python", "HTML"],
#   ]
#   results = [0, 0, 1]
#
# Sample Output:
#   "Python"


# Solution: Single pass, track running leader
# Time: O(n) | Space: O(k)
#   n = number of competitions, k = number of teams
#
# Walk the competitions in order. For each one, look up the winning team from
# the result (1 = home team in slot 0, 0 = away team in slot 1), add 3 points
# to that team's running total in a dict, and update the best-so-far if the
# new total beats it. Tracking the leader incrementally avoids a second pass
# over the dict at the end.
def tournamentWinner(competitions, results):
    # Write your code here.
    points = {}
    best_k = -1
    best_v = -1
    for duel, result in zip(competitions, results):
        if result:
            cand = duel[0]
            if cand in points:
                points[cand] += 3
            else:
                points[cand] = 3

            if points[cand] > best_v:
                best_v = points[cand]
                best_k = cand
        else:
            cand = duel[1]
            if cand in points:
                points[cand] += 3
            else:
                points[cand] = 3

            if points[cand] > best_v:
                best_v = points[cand]
                best_k = cand

    return best_k
