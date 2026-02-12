"""
Tests for LeetCode 133: Clone Graph
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from graph.clone_graph import Solution, Node


class TestCloneGraph:
    """Test cases for Clone Graph problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]
        
        cloned = self.solution.cloneGraph(node1)
        assert cloned is not None
        assert cloned.val == 1
        assert cloned is not node1

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.cloneGraph(None) is None
