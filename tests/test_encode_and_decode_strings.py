"""
Tests for LeetCode 271: Encode and Decode Strings
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from string.encode_and_decode_strings import Codec


class TestEncodeAndDecodeStrings:
    """Test cases for Encode and Decode Strings problem"""

    def test_example_1(self):
        """Test case from example 1"""
        codec = Codec()
        strs = ["Hello", "World"]
        encoded = codec.encode(strs)
        decoded = codec.decode(encoded)
        assert decoded == strs

    def test_example_2(self):
        """Test case from example 2"""
        codec = Codec()
        strs = [""]
        encoded = codec.encode(strs)
        decoded = codec.decode(encoded)
        assert decoded == strs
