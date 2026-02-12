"""
Tests for LeetCode 73: Set Matrix Zeroes
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from matrix.set_matrix_zeroes import Solution


class TestSetMatrixZeroes:
    """Test cases for Set Matrix Zeroes problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        self.solution.setZeroes(matrix)
        assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    def test_example_2(self):
        """Test case from example 2"""
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        self.solution.setZeroes(matrix)
        assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
