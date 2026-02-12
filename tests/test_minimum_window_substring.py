"""
Tests for LeetCode 76: Minimum Window Substring
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from string.minimum_window_substring import Solution


class TestMinimumWindowSubstring:
    """Test cases for Minimum Window Substring problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.minWindow("a", "a") == "a"
