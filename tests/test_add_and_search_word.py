"""
Tests for LeetCode 211: Design Add and Search Words Data Structure
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from tree.add_and_search_word import WordDictionary


class TestAddAndSearchWord:
    """Test cases for Add and Search Word problem"""

    def test_example_1(self):
        """Test case from example 1"""
        wordDictionary = WordDictionary()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")
        assert wordDictionary.search("pad") == False
        assert wordDictionary.search("bad") == True
        assert wordDictionary.search(".ad") == True
        assert wordDictionary.search("b..") == True
