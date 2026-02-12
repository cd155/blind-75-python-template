"""
Tests for LeetCode 217: Contains Duplicate
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from array.contains_duplicate import Solution


class TestContainsDuplicate:
    """Test cases for contains duplicate problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.containsDuplicate([1, 2, 3, 1]) == True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.containsDuplicate([1, 2, 3, 4]) == False
