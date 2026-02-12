"""
Tests for LeetCode 1143: Longest Common Subsequence
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from dynamic_programming.longest_common_subsequence import Solution


class TestLongestCommonSubsequence:
    """Test cases for longest common subsequence problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.longestCommonSubsequence("abcde", "ace") == 3

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.longestCommonSubsequence("abc", "abc") == 3
