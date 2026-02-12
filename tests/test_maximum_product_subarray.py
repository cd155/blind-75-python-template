"""
Tests for LeetCode 152: Maximum Product Subarray
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from array.maximum_product_subarray import Solution


class TestMaximumProductSubarray:
    """Test cases for maximum product subarray problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.maxProduct([2, 3, -2, 4]) == 6

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.maxProduct([-2, 0, -1]) == 0
