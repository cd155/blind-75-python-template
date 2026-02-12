"""
Tests for LeetCode 53: Maximum Subarray
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from array.maximum_subarray import Solution


class TestMaximumSubarray:
    """Test cases for maximum subarray problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.maxSubArray([1]) == 1
