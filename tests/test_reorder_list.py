"""
Tests for LeetCode 143: Reorder List
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from linked_list.reorder_list import Solution, ListNode


class TestReorderList:
    """Test cases for Reorder List problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        self.solution.reorderList(head)
        assert head.val == 1
        assert head.next.val == 4

    def test_example_2(self):
        """Test case from example 2"""
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.solution.reorderList(head)
        assert head.val == 1
        assert head.next.val == 5
