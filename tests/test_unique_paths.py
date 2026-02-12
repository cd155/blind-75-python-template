"""
Tests for LeetCode 62: Unique Paths
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from dynamic_programming.unique_paths import Solution


class TestUniquePaths:
    """Test cases for unique paths problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.uniquePaths(3, 7) == 28

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.uniquePaths(3, 2) == 3
