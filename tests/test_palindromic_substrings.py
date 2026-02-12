"""
Tests for LeetCode 647: Palindromic Substrings
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from string.palindromic_substrings import Solution


class TestPalindromicSubstrings:
    """Test cases for Palindromic Substrings problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.countSubstrings("abc") == 3

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.countSubstrings("aaa") == 6
