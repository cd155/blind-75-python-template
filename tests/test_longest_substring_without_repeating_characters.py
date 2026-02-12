"""
Tests for LeetCode 3: Longest Substring Without Repeating Characters
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from string.longest_substring_without_repeating_characters import Solution


class TestLongestSubstringWithoutRepeatingCharacters:
    """Test cases for Longest Substring Without Repeating Characters problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.lengthOfLongestSubstring("abcabcbb") == 3

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.lengthOfLongestSubstring("bbbbb") == 1
