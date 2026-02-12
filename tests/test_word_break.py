"""
Tests for LeetCode 139: Word Break
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from dynamic_programming.word_break import Solution


class TestWordBreak:
    """Test cases for word break problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.wordBreak("leetcode", ["leet", "code"]) == True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.wordBreak("applepenapple", ["apple", "pen"]) == True
