"""
Tests for LeetCode 235: Lowest Common Ancestor of a Binary Search Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from tree.lowest_common_ancestor_of_a_bst import Solution, TreeNode


class TestLowestCommonAncestorOfBST:
    """Test cases for Lowest Common Ancestor of a BST problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
        p = root.left
        q = root.right
        result = self.solution.lowestCommonAncestor(root, p, q)
        assert result.val == 6

    def test_example_2(self):
        """Test case from example 2"""
        root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
        p = root.left
        q = root.left.right
        result = self.solution.lowestCommonAncestor(root, p, q)
        assert result.val == 2
