"""
Tests for LeetCode 295: Find Median from Data Stream
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from heap.find_median_from_data_stream import MedianFinder


class TestFindMedianFromDataStream:
    """Test cases for Find Median from Data Stream problem"""

    def test_example_1(self):
        """Test case from example 1"""
        medianFinder = MedianFinder()
        medianFinder.addNum(1)
        medianFinder.addNum(2)
        assert medianFinder.findMedian() == 1.5
        medianFinder.addNum(3)
        assert medianFinder.findMedian() == 2.0
