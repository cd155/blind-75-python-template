"""
Tests for LeetCode 49: Group Anagrams
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from string.group_anagrams import Solution


class TestGroupAnagrams:
    """Test cases for Group Anagrams problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        result_sorted = [sorted(group) for group in result]
        expected = [sorted(["bat"]), sorted(["nat", "tan"]), sorted(["ate", "eat", "tea"])]
        assert sorted(result_sorted) == sorted(expected)

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.groupAnagrams([""]) == [[""]]
