"""
Tests for LeetCode 55: Jump Game
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from dynamic_programming.jump_game import Solution


class TestJumpGame:
    """Test cases for jump game problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.canJump([2, 3, 1, 1, 4]) == True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.canJump([3, 2, 1, 0, 4]) == False
