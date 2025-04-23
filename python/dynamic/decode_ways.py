# https://leetcode.com/problems/decode-ways/description/
"""
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"

Output: 3

Explanation:

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"

Output: 0

Explanation:

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""
from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1  # Base case: one way to decode an empty string

        # eg: 1126
        # 0 0 0 0 1
        # 0 0 0 1 1
        # 0 0 2 1 1
        # 0 3 2 1 1
        # 5 3 2 1 1
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0  # No way to decode a string starting with '0'
            else:
                # Take one digit
                dp[i] = dp[i + 1]

                # Take two digits if valid from i to i + 1
                if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
                    dp[i] += dp[i + 2]

        return dp[0]

class SolutionRecursive:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(maxsize=None)
        def dp(i):
            # Base case: one way to decode an empty string
            if i == n:
                return 1
            if s[i] == '0':
                # No way to decode a string starting with '0'
                return 0
            else:
                result = dp(i + 1)
                
                # Take two digit if valid
                if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
                    result += dp(i + 2)
                
                return result
        
        return dp(0)
    
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture(params=[Solution, SolutionRecursive],
               ids=["Iterative", "Recursive"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    s = "12"
    expected = 2  # can be decoded as "AB" (1,2) or "L" (12)
    assert solution_instance.numDecodings(s) == expected

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    s = "226"
    expected = 3  # can be decoded as "BZ" (2,26), "VF" (22,6), or "BBF" (2,2,6)
    assert solution_instance.numDecodings(s) == expected

def test_example3(solution_instance):
    """Test Example 3 from the problem description."""
    s = "06"
    expected = 0  # invalid due to leading zero
    assert solution_instance.numDecodings(s) == expected

def test_single_digit(solution_instance):
    """Test with single valid digit."""
    s = "5"
    expected = 1  # only one way: "E"
    assert solution_instance.numDecodings(s) == expected

def test_zero(solution_instance):
    """Test with single zero."""
    s = "0"
    expected = 0  # invalid encoding
    assert solution_instance.numDecodings(s) == expected

def test_multiple_zeros(solution_instance):
    """Test with multiple zeros."""
    s = "000"
    expected = 0  # invalid encoding
    assert solution_instance.numDecodings(s) == expected

def test_valid_with_zeros(solution_instance):
    """Test valid string with zeros."""
    s = "101"
    expected = 1  # only one way: "JA"
    assert solution_instance.numDecodings(s) == expected

def test_multiple_ways_with_zero(solution_instance):
    """Test multiple decodings with zero."""
    s = "1201"
    expected = 1  # only one way: "ABA"
    assert solution_instance.numDecodings(s) == expected

def test_consecutive_ones(solution_instance):
    """Test with consecutive ones."""
    s = "1111"
    expected = 5  # "AAAA", "LAA", "ALA", "AAL", "LL"
    assert solution_instance.numDecodings(s) == expected

def test_boundary_values(solution_instance):
    """Test with boundary values (1 and 26)."""
    s = "126"
    expected = 3  # "ABF", "LF", "AF"
    assert solution_instance.numDecodings(s) == expected

def test_invalid_two_digit(solution_instance):
    """Test with invalid two-digit numbers."""
    s = "27"
    expected = 1  # only one way: "BG"
    assert solution_instance.numDecodings(s) == expected

def test_long_valid_string(solution_instance):
    """Test with longer valid string."""
    s = "11111"
    expected = 8  # Various combinations
    assert solution_instance.numDecodings(s) == expected

def test_all_valid_pairs(solution_instance):
    """Test with all valid two-digit numbers."""
    s = "123456"
    expected = 3  # Multiple valid ways
    assert solution_instance.numDecodings(s) == expected

def test_invalid_middle_zero(solution_instance):
    """Test with invalid zero in middle."""
    s = "1012"
    expected = 2
    assert solution_instance.numDecodings(s) == expected

def test_maximum_length(solution_instance):
    """Test with maximum length string (100)."""
    s = "1" * 100
    result = solution_instance.numDecodings(s)
    assert result > 0  # Should have at least one valid decoding

def test_alternating_digits(solution_instance):
    """Test with alternating digits."""
    s = "121212"
    expected = 13  # Multiple valid combinations
    assert solution_instance.numDecodings(s) == expected

def test_mixed_valid_invalid(solution_instance):
    """Test with mix of valid and invalid combinations."""
    s = "2611055"
    expected = 2  # Limited valid combinations due to '0'
    assert solution_instance.numDecodings(s) == expected