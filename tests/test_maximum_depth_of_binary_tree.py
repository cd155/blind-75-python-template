"""
Tests for LeetCode 104: Maximum Depth of Binary Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from tree.maximum_depth_of_binary_tree import Solution, TreeNode


class TestMaximumDepthOfBinaryTree:
    """Test cases for Maximum Depth of Binary Tree problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        assert self.solution.maxDepth(root) == 3

    def test_example_2(self):
        """Test case from example 2"""
        root = TreeNode(1, None, TreeNode(2))
        assert self.solution.maxDepth(root) == 2
