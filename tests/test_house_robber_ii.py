"""
Tests for LeetCode 213: House Robber II
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from dynamic_programming.house_robber_ii import Solution


class TestHouseRobberIi:
    """Test cases for house robber ii problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.rob([2, 3, 2]) == 3

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.rob([1, 2, 3, 1]) == 4
