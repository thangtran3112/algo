# https://leetcode.com/problems/read-n-characters-given-read4/
"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

# Global state for the mock file and pointer
from typing import List
import pytest

mock_file_content = ""
mock_file_pointer = 0

def set_mock_file(content: str):
    """Resets the mock file content and pointer."""
    global mock_file_content, mock_file_pointer
    mock_file_content = content
    mock_file_pointer = 0

def read4(buf4: List[str]) -> int:
    """Mock implementation of the read4 API."""
    global mock_file_content, mock_file_pointer
    
    count = 0
    while count < 4 and mock_file_pointer < len(mock_file_content):
        buf4[count] = mock_file_content[mock_file_pointer]
        mock_file_pointer += 1
        count += 1
        
    return count

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        pointer = 0
        remaining = n
        while remaining > 0:
            buf4 = [''] * 4
            letters_read = read4(buf4)
            for i in range(letters_read):
                if pointer < n:
                    buf[pointer] = buf4[i]
                    pointer += 1
            remaining -= 4
        return pointer
    
# === TEST CASES ===

def test_example1():
    """Test reading from file "abcdefghijk" with different n values."""
    set_mock_file("abcdefghijk")
    sol = Solution()
    
    # Read 4 characters
    buf = [''] * 10
    count = sol.read(buf, 4)
    assert count == 4
    assert "".join(buf[:count]) == "abcd"
    
    # Reset for next test
    set_mock_file("abcdefghijk")
    
    # Read 6 characters
    buf = [''] * 10
    count = sol.read(buf, 6)
    assert count == 6
    assert "".join(buf[:count]) == "abcdef"
    
    # Reset for next test
    set_mock_file("abcdefghijk")
    
    # Read all characters
    buf = [''] * 20
    count = sol.read(buf, 11)
    assert count == 11
    assert "".join(buf[:count]) == "abcdefghijk"

def test_read_more_than_available():
    """Test reading more characters than are available in the file."""
    set_mock_file("abc")
    sol = Solution()
    
    buf = [''] * 10
    count = sol.read(buf, 5)
    assert count == 3
    assert "".join(buf[:count]) == "abc"

def test_empty_file():
    """Test reading from an empty file."""
    set_mock_file("")
    sol = Solution()
    
    buf = [''] * 5
    count = sol.read(buf, 5)
    assert count == 0
    assert "".join(buf[:count]) == ""

def test_read_zero():
    """Test reading 0 characters."""
    set_mock_file("abcde")
    sol = Solution()
    
    buf = [''] * 5
    count = sol.read(buf, 0)
    assert count == 0
    assert "".join(buf[:count]) == ""

def test_exact_multiples_of_4():
    """Test when file length is exactly divisible by 4."""
    set_mock_file("abcdefgh")  # 8 characters
    sol = Solution()
    
    buf = [''] * 8
    count = sol.read(buf, 8)
    assert count == 8
    assert "".join(buf[:count]) == "abcdefgh"

def test_read_one_by_one():
    """Test reading one character at a time."""
    set_mock_file("abcde")
    sol = Solution()
    
    expected_chars = "abcde"
    for i, expected_char in enumerate(expected_chars):
        # Reset for each character read
        set_mock_file(expected_chars)
        buf = [''] * (i+1)
        # Read only up to the current position
        count = sol.read(buf, i+1)
        assert count == i+1
        assert "".join(buf[:count]) == expected_chars[:i+1]

def test_large_n():
    """Test with a large n value."""
    set_mock_file("abc")
    sol = Solution()
    
    buf = [''] * 1000
    count = sol.read(buf, 1000)
    assert count == 3
    assert "".join(buf[:count]) == "abc"

def test_large_file():
    """Test with a large file."""
    large_content = "a" * 1000
    set_mock_file(large_content)
    sol = Solution()
    
    buf = [''] * 1000
    count = sol.read(buf, 1000)
    assert count == 1000
    assert "".join(buf[:count]) == large_content

def test_large_file_small_read():
    """Test reading a small portion of a large file."""
    large_content = "a" * 500 + "b" * 500
    set_mock_file(large_content)
    sol = Solution()
    
    buf = [''] * 10
    count = sol.read(buf, 10)
    assert count == 10
    assert "".join(buf[:count]) == "a" * 10