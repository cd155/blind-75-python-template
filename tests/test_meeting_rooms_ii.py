"""
Tests for LeetCode 253: Meeting Rooms II
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from interval.meeting_rooms_ii import Solution


class TestMeetingRoomsII:
    """Test cases for Meeting Rooms II problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.minMeetingRooms([[7, 10], [2, 4]]) == 1
