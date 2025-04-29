"""
Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.

Method read4:

The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf4
    Returns:    int

buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].
Below is a high-level example of how read4 works:


File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
char[] buf4 = new char[4]; // Create buffer with enough space to store characters
read4(buf4); // read4 returns 4. Now buf4 = "abcd", fp points to 'e'
read4(buf4); // read4 returns 1. Now buf4 = "e", fp points to end of file
read4(buf4); // read4 returns 0. Now buf4 = "", fp points to end of file
 

Method read:

By using the read4 method, implement the method read that reads n characters from file and store it in the buffer array buf. Consider that you cannot manipulate file directly.

The return value is the number of actual characters read.

Definition of read:

    Parameters:	char[] buf, int n
    Returns:	int

buf[] is a destination, not a source. You will need to write the results to buf[].
Note:

Consider that you cannot manipulate the file directly. The file is only accessible for read4 but not for read.
The read function may be called multiple times.
Please remember to RESET your class variables declared in Solution, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
It is guaranteed that in a given test case the same buffer buf is called by read.
 

Example 1:

Input: file = "abc", queries = [1,2,1]
Output: [1,2,0]
Explanation: The test case represents the following scenario:
File file("abc");
Solution sol;
sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.
Example 2:

Input: file = "abc", queries = [4,1]
Output: [3,0]
Explanation: The test case represents the following scenario:
File file("abc");
Solution sol;
sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
 

Constraints:

1 <= file.length <= 500
file consist of English letters and digits.
1 <= queries.length <= 10
1 <= queries[i] <= 500
"""
# === TEST CASES ===
import collections
from typing import List
import pytest

# Global state for the mock file and pointer
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
    def __init__(self):
        self.to_load = collections.deque()  # this is used to analyze data in buf4

    def read(self, buf: List[str], n: int) -> int:
        read_count = 0
        buf4 = [''] * 4
        while read_count < n:  # main logic: read until arrive at n
            if len(self.to_load) > 0:  # load from buffer to buf
                buf[read_count] = self.to_load.popleft()  # O(1)
                read_count += 1
            else:  # load file to buf4
                for i in range(read4(buf4)):
                    self.to_load.append(buf4[i])
                if len(self.to_load) == 0:  # edge case, nothing to load(even read_count not reach n yet)
                    break
        return read_count

# === TEST CASES ===

def test_example1():
    """Test Example 1 from the problem description."""
    set_mock_file("abc")
    sol = Solution()
    
    # First query: read 1 character
    buf1 = [''] * 1
    count1 = sol.read(buf1, 1)
    assert count1 == 1
    assert "".join(buf1) == "a"
    
    # Second query: read 2 characters
    buf2 = [''] * 2
    count2 = sol.read(buf2, 2)
    assert count2 == 2
    assert "".join(buf2) == "bc"
    
    # Third query: read 1 character (EOF)
    buf3 = [''] * 1
    count3 = sol.read(buf3, 1)
    assert count3 == 0
    assert "".join(buf3) == ""

def test_example2():
    """Test Example 2 from the problem description."""
    set_mock_file("abc")
    sol = Solution()
    
    # First query: read 4 characters (only 3 available)
    buf1 = [''] * 4
    count1 = sol.read(buf1, 4)
    assert count1 == 3
    assert "".join(buf1[:count1]) == "abc"
    
    # Second query: read 1 character (EOF)
    buf2 = [''] * 1
    count2 = sol.read(buf2, 1)
    assert count2 == 0
    assert "".join(buf2[:count2]) == ""

def test_empty_file():
    """Test with an empty file."""
    set_mock_file("")
    sol = Solution()
    
    buf = [''] * 5
    count = sol.read(buf, 5)
    assert count == 0
    assert "".join(buf[:count]) == ""

def test_multiple_read4_calls():
    """Test when multiple read4 calls are needed."""
    set_mock_file("abcdefghij")  # 10 characters
    sol = Solution()
    
    # First read: 6 characters
    buf1 = [''] * 6
    count1 = sol.read(buf1, 6)
    assert count1 == 6
    assert "".join(buf1) == "abcdef"
    
    # Second read: 5 characters (only 4 left)
    buf2 = [''] * 5
    count2 = sol.read(buf2, 5)
    assert count2 == 4
    assert "".join(buf2[:count2]) == "ghij"
    
    # Third read: EOF
    buf3 = [''] * 3
    count3 = sol.read(buf3, 3)
    assert count3 == 0
    assert "".join(buf3[:count3]) == ""

def test_small_reads():
    """Test with a series of small reads."""
    set_mock_file("abcdefgh")  # 8 characters
    sol = Solution()
    
    # Four reads of 1 character each
    for i, expected in enumerate("abcd"):
        buf = [''] * 1
        count = sol.read(buf, 1)
        assert count == 1
        assert buf[0] == expected
        
    # One read of 4 characters
    buf = [''] * 4
    count = sol.read(buf, 4)
    assert count == 4
    assert "".join(buf) == "efgh"
    
    # Final read (EOF)
    buf = [''] * 1
    count = sol.read(buf, 1)
    assert count == 0

def test_zero_length_read():
    """Test reading zero characters."""
    set_mock_file("abcde")
    sol = Solution()
    
    # Read 0 characters
    buf = [''] * 5
    count = sol.read(buf, 0)
    assert count == 0
    assert "".join(buf[:count]) == ""
    
    # Then read 3
    buf = [''] * 3
    count = sol.read(buf, 3)
    assert count == 3
    assert "".join(buf) == "abc"

def test_larger_buffer_than_file():
    """Test when the requested read is larger than the file."""
    set_mock_file("abcdefgh")  # 8 characters
    sol = Solution()
    
    # Try to read 20 characters
    buf = [''] * 20
    count = sol.read(buf, 20)
    assert count == 8
    assert "".join(buf[:count]) == "abcdefgh"
    
    # Try to read more
    buf = [''] * 5
    count = sol.read(buf, 5)
    assert count == 0
    assert "".join(buf[:count]) == ""

def test_exactly_four_chars():
    """Test when reading exactly 4 characters."""
    set_mock_file("abcd")
    sol = Solution()
    
    buf = [''] * 4
    count = sol.read(buf, 4)
    assert count == 4
    assert "".join(buf) == "abcd"
    
    # Try to read more
    buf = [''] * 2
    count = sol.read(buf, 2)
    assert count == 0
    assert "".join(buf[:count]) == ""

def test_reading_across_read4_boundaries():
    """Test reading across read4 boundaries."""
    set_mock_file("abcdefgh")  # 8 characters
    sol = Solution()
    
    # Read 3 characters
    buf1 = [''] * 3
    count1 = sol.read(buf1, 3)
    assert count1 == 3
    assert "".join(buf1) == "abc"
    
    # Read 3 more (crosses read4 boundary)
    buf2 = [''] * 3
    count2 = sol.read(buf2, 3)
    assert count2 == 3
    assert "".join(buf2) == "def"
    
    # Read remaining 2
    buf3 = [''] * 2
    count3 = sol.read(buf3, 2)
    assert count3 == 2
    assert "".join(buf3) == "gh"

def test_at_file_boundaries():
    """Test reading at the boundaries of the file."""
    set_mock_file("abc")
    sol = Solution()
    
    # Read all 3 characters
    buf1 = [''] * 3
    count1 = sol.read(buf1, 3)
    assert count1 == 3
    assert "".join(buf1) == "abc"
    
    # Try reading 0 at EOF
    buf2 = [''] * 1
    count2 = sol.read(buf2, 0)
    assert count2 == 0
    assert "".join(buf2[:count2]) == ""
    
    # Try reading more at EOF
    buf3 = [''] * 1
    count3 = sol.read(buf3, 1)
    assert count3 == 0
    assert "".join(buf3[:count3]) == ""

def test_long_file():
    """Test with a longer file."""
    long_content = "abcdefghijklmnopqrstuvwxyz" * 5  # 130 characters
    set_mock_file(long_content)
    sol = Solution()
    
    # Read 50 characters
    buf1 = [''] * 50
    count1 = sol.read(buf1, 50)
    assert count1 == 50
    assert "".join(buf1) == long_content[:50]
    
    # Read 70 more
    buf2 = [''] * 70
    count2 = sol.read(buf2, 70)
    assert count2 == 70
    assert "".join(buf2) == long_content[50:120]
    
    # Read remaining 10
    buf3 = [''] * 20
    count3 = sol.read(buf3, 20)
    assert count3 == 10
    assert "".join(buf3[:count3]) == long_content[120:130]
    
    # Try reading more
    buf4 = [''] * 10
    count4 = sol.read(buf4, 10)
    assert count4 == 0
    assert "".join(buf4[:count4]) == ""