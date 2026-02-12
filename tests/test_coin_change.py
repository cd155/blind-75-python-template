"""
Tests for LeetCode 322: Coin Change
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from dynamic_programming.coin_change import Solution


class TestCoinChange:
    """Test cases for coin change problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.coinChange([1, 2, 5], 11) == 3

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.coinChange([2], 3) == -1
