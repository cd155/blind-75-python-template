"""
Tests for LeetCode 102: Binary Tree Level Order Traversal
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from tree.binary_tree_level_order_traversal import Solution, TreeNode


class TestBinaryTreeLevelOrderTraversal:
    """Test cases for Binary Tree Level Order Traversal problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        assert self.solution.levelOrder(root) == [[3], [9, 20], [15, 7]]

    def test_example_2(self):
        """Test case from example 2"""
        root = TreeNode(1)
        assert self.solution.levelOrder(root) == [[1]]
