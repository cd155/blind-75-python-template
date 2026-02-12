"""
Tests for LeetCode 98: Validate Binary Search Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from tree.validate_binary_search_tree import Solution, TreeNode


class TestValidateBinarySearchTree:
    """Test cases for Validate Binary Search Tree problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        assert self.solution.isValidBST(root) == True

    def test_example_2(self):
        """Test case from example 2"""
        root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        assert self.solution.isValidBST(root) == False
