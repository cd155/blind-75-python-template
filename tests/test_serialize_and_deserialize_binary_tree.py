"""
Tests for LeetCode 297: Serialize and Deserialize Binary Tree
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from tree.serialize_and_deserialize_binary_tree import Codec, TreeNode


class TestSerializeAndDeserializeBinaryTree:
    """Test cases for Serialize and Deserialize Binary Tree problem"""

    def test_example_1(self):
        """Test case from example 1"""
        codec = Codec()
        root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        serialized = codec.serialize(root)
        deserialized = codec.deserialize(serialized)
        assert deserialized.val == 1

    def test_example_2(self):
        """Test case from example 2"""
        codec = Codec()
        serialized = codec.serialize(None)
        deserialized = codec.deserialize(serialized)
        assert deserialized is None
