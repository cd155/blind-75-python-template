"""
Tests for LeetCode 338: Counting Bits
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from binary.counting_bits import Solution


class TestCountingBits:
    """Test cases for counting bits problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.countBits(2) == [0, 1, 1]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.countBits(5) == [0, 1, 1, 2, 1, 2]
