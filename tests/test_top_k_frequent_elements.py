"""
Tests for LeetCode 347: Top K Frequent Elements
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from heap.top_k_frequent_elements import Solution


class TestTopKFrequentElements:
    """Test cases for Top K Frequent Elements problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
        assert sorted(result) == [1, 2]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.topKFrequent([1], 1) == [1]
