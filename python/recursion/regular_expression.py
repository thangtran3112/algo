# https://leetcode.com/problems/regular-expression-matching/description/
"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""
from functools import lru_cache


class SolutionRecursive:
    # missisipi and miisip*i
    # note the when i = 2, j = 2. j+1 =3, and if we choose zero of s* ,
    # we need to check s[2:] to be matched with p[j+2:], which is isip*i vs ssisipi
    def isMatch(self, s: str, pattern: str) -> bool:
        # matching s[i:] with patter[j:]
        @lru_cache(maxsize=None)
        def dp(i, j):
            # base case, able to walkthrough both s and pattern at the end
            if j == len(pattern):
                return i == len(s)

            first_match = i < len(s) and pattern[j] in {s[i], '.'}

            # checking for matching zero or more (*)
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                # case 1: assuming zero of s[i], matching ssisipi with isip*i
                case1 = dp(i, j + 2)
                if case1:
                    return True
                # case 2: match first character, match next: sisipi and s*isip*i
                return first_match and dp(i + 1, j)
            else:
                return first_match and dp(i + 1, j + 1)

        return dp(0, 0)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        row_size = len(s)
        col_size = len(p)
        # dp[i][j] means there is a match for s[i:] with p[j:]
        dp = [[False] * (col_size + 1) for _ in range(row_size + 1)]
        # initially dp[row_size][col_size] = True, empty string match with empty string
        dp[row_size][col_size] = True

        # start from bottom row
        for i in range(row_size, -1, -1):
            # we need to compute d[i][j + 2], collumn will start from col_size - 1
            for j in range(col_size - 1, -1, -1):
                first_match = i < row_size and (p[j] == s[i] or p[j] == '.')
                if j + 1 < col_size and p[j + 1] == '*':
                    # case 1: assuming zero of s[i], checking s[i] with p[j + 2]
                    # case 2: first match, and skip (a*) in pattern, skip 2 character in pattern p
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    # normal match when there is no *
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]
    
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture(params=[SolutionRecursive, Solution],
               ids=["Recursive", "DP"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    s = "aa"
    p = "a"
    assert not solution_instance.isMatch(s, p)

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    s = "aa"
    p = "a*"
    assert solution_instance.isMatch(s, p)

def test_example3(solution_instance):
    """Test Example 3 from the problem description."""
    s = "ab"
    p = ".*"
    assert solution_instance.isMatch(s, p)

def test_empty_string(solution_instance):
    """Test matching empty string."""
    assert solution_instance.isMatch("", "")
    assert not solution_instance.isMatch("", "a")
    assert solution_instance.isMatch("", "a*")
    assert solution_instance.isMatch("", ".*")

def test_dot_operator(solution_instance):
    """Test the dot operator matching."""
    assert solution_instance.isMatch("a", ".")
    assert solution_instance.isMatch("b", ".")
    assert solution_instance.isMatch("abc", "...")
    assert not solution_instance.isMatch("abc", "..")

def test_star_operator(solution_instance):
    """Test the star operator matching."""
    assert solution_instance.isMatch("aaa", "a*")
    assert solution_instance.isMatch("", "a*")
    assert solution_instance.isMatch("a", "a*")
    assert not solution_instance.isMatch("aa", "a*b")

def test_dot_star_combination(solution_instance):
    """Test combinations of dot and star operators."""
    assert solution_instance.isMatch("abc", ".*c")
    assert solution_instance.isMatch("abcd", ".*d")
    assert solution_instance.isMatch("abc", "a.*c")
    assert not solution_instance.isMatch("abc", "a.*d")

def test_complex_patterns(solution_instance):
    """Test more complex pattern matching."""
    assert solution_instance.isMatch("aab", "c*a*b")
    assert solution_instance.isMatch("mississippi", "mis*is*ip*i")
    assert not solution_instance.isMatch("mississippi", "mis*is*p*.")

def test_multiple_stars(solution_instance):
    """Test patterns with multiple consecutive stars."""
    assert solution_instance.isMatch("aaa", "a*a*a*")
    assert solution_instance.isMatch("b", "a*b*c*")
    assert solution_instance.isMatch("abc", "a*b*c*")
    assert not solution_instance.isMatch("abc", "a*b*d*")

def test_edge_cases(solution_instance):
    """Test edge cases and boundary conditions."""
    # Maximum length strings (20 characters)
    s = "a" * 20
    p = "a*" * 10
    assert solution_instance.isMatch(s, p)
    
    # Single character with multiple possibilities
    assert solution_instance.isMatch("a", "ab*")
    assert not solution_instance.isMatch("a", "ab*c")

def test_mixed_patterns(solution_instance):
    """Test mixed patterns with dots, stars, and literals."""
    assert solution_instance.isMatch("abcd", "a.*d")
    assert solution_instance.isMatch("abcd", ".*.*.*.*")
    assert solution_instance.isMatch("abcd", "a*b*c*d*")
    assert not solution_instance.isMatch("abcd", "a.*e")

def test_alternating_patterns(solution_instance):
    """Test patterns with alternating characters."""
    assert solution_instance.isMatch("xaxbxc", "x.*x.*x.*")
    assert solution_instance.isMatch("xaxbxc", "x.x.x.")
    assert not solution_instance.isMatch("xaxbxc", "x.x.x.x")

def test_boundary_cases(solution_instance):
    """Test boundary cases with minimum and maximum lengths."""
    # Single character tests
    assert solution_instance.isMatch("a", "a")
    assert solution_instance.isMatch("a", ".*")
    assert not solution_instance.isMatch("a", "b")
    
    # Maximum length pattern with minimum length string
    p = ".*" * 10  # 20 characters
    s = "a"
    assert solution_instance.isMatch(s, p)