"""
Tests for LeetCode 79: Word Search
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from matrix.word_search import Solution


class TestWordSearch:
    """Test cases for Word Search problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        assert self.solution.exist(board, "ABCCED") == True

    def test_example_2(self):
        """Test case from example 2"""
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        assert self.solution.exist(board, "SEE") == True
