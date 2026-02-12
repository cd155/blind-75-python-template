"""
Tests for LeetCode 128: Longest Consecutive Sequence
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from graph.longest_consecutive_sequence import Solution


class TestLongestConsecutiveSequence:
    """Test cases for Longest Consecutive Sequence problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
