"""
Tests for LeetCode 20: Valid Parentheses
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from string.valid_parentheses import Solution


class TestValidParentheses:
    """Test cases for Valid Parentheses problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.isValid("()") == True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.isValid("()[]{}") == True

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.isValid("(]") == False
