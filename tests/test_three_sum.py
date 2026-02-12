"""
Tests for LeetCode 15: 3Sum
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from array.three_sum import Solution


class TestThreeSum:
    """Test cases for 3sum problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.threeSum([0, 1, 1]) == []
