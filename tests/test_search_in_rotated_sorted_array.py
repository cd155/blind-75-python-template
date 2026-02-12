"""
Tests for LeetCode 33: Search in Rotated Sorted Array
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from array.search_in_rotated_sorted_array import Solution


class TestSearchInRotatedSortedArray:
    """Test cases for search in rotated sorted array problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
