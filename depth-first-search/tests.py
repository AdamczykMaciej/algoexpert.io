# Tests for Depth-First Search
#
# Run with:   python -m unittest tests.py
#         or: python tests.py

import unittest

from main import Node


class TestDepthFirstSearch(unittest.TestCase):
    def test_sample_input(self):
        # The example from the problem statement.
        #             A
        #         / | | \
        #        B  C D  E
        #       / \    / \
        #      F   G  H  I
        #         / \
        #        J   K
        A = Node("A")
        A.addChild("B").addChild("C").addChild("D").addChild("E")
        B = A.children[0]
        B.addChild("F").addChild("G")
        G = B.children[1]
        G.addChild("J").addChild("K")
        D = A.children[2]
        D.addChild("H").addChild("I")

        self.assertEqual(
            A.depthFirstSearch([]),
            ["A", "B", "F", "G", "J", "K", "C", "D", "H", "I", "E"],
        )

    def test_single_node(self):
        # Root with no children — only its own name.
        root = Node("only")
        self.assertEqual(root.depthFirstSearch([]), ["only"])

    def test_flat_tree(self):
        # Root with children but no grandchildren — left-to-right after root.
        root = Node("R")
        root.addChild("a").addChild("b").addChild("c")
        self.assertEqual(root.depthFirstSearch([]), ["R", "a", "b", "c"])

    def test_linear_chain(self):
        # Each node has exactly one child — chain of length 4.
        root = Node("1")
        cur = root
        for name in ["2", "3", "4"]:
            cur.addChild(name)
            cur = cur.children[0]
        self.assertEqual(root.depthFirstSearch([]), ["1", "2", "3", "4"])

    def test_left_to_right_ordering(self):
        # Two subtrees — make sure the left one is fully explored before
        # touching the right one.
        #         R
        #        / \
        #       L   R'
        #      /|   |\
        #     a b   c d
        root = Node("R")
        root.addChild("L").addChild("R'")
        root.children[0].addChild("a").addChild("b")
        root.children[1].addChild("c").addChild("d")
        self.assertEqual(
            root.depthFirstSearch([]),
            ["R", "L", "a", "b", "R'", "c", "d"],
        )

    def test_appends_to_existing_array(self):
        # Method should append to whatever array is passed in, not replace it.
        root = Node("X")
        root.addChild("Y")
        self.assertEqual(root.depthFirstSearch(["pre"]), ["pre", "X", "Y"])

    def test_returns_same_array(self):
        # The returned array should be the same object that was passed in
        # (the method mutates and returns it).
        root = Node("only")
        original = []
        result = root.depthFirstSearch(original)
        self.assertIs(result, original)


if __name__ == "__main__":
    unittest.main()
