"""
Tests for LeetCode 435: Non-overlapping Intervals
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from interval.non_overlapping_intervals import Solution


class TestNonOverlappingIntervals:
    """Test cases for Non-overlapping Intervals problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
