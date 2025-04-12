# https://leetcode.com/problems/longest-common-subsequence/description/
"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""

from functools import lru_cache

# 2D Dynamic Programming
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
            * Start from bottom last row and last collumn to build lcs
            * if first letter is not the same: 
                lcs[row, col] = max(lcs[row, col + 1],lcs[row+1, col])
            * if first letter is the same:
                lcs[row, col] = 1 + lcs[row + 1, col + 1]
            * Example: lcs[row, col] is the lcs between text1[row:] and text2[col:]
               g  t  g  t  g  a   t c
            a
            c
            t       max --
            g        |
            a
            t
            t
            a
        """
        # Make a grid of 0's with len(text2) + 1 columns and len(text1) + 1 rows.
        # do not use [[0]*cols] * rows. It will create rows of same object reference
        # Same as: dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        # Note: row = len(text1) or col = len(text2) → we will be out-of-bound for
        # last row and last col. Thus we need dp_grid[len(text1) + 1][len(text2) + 1]
        dp_grid = []
        for _ in range(len(text1) + 1):
            row_arr = []
            for _ in range(len(text2) + 1):
                row_arr.append(0)
            dp_grid.append(row_arr)

        # Iterate from last collumn and last row
        for row in reversed(range(len(text1))):
            for col in reversed(range(len(text2))):
                # same letter starting for both sequences
                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])

        return dp_grid[0][0]

class SolutionUnoptimizeRecursive:
    """
    define function LCS(text1, text2):
    # If either string is empty there can be no common subsequence
    if length of text1 or text2 is 0:
        return 0

    letter1 = the first letter in text1

    # The case where the line *is not* part of the optimal solution
    case1 = LCS(text1.substring(1), text2)

    case2 = 0
    if letter1 is in text2:
        firstOccurence = first position of letter1 in text2
        # The case where the line *is* part of the optimal solution
        case2 = 1 + LCS(text1.substring(1), text2.substring(firstOccurence + 1))

    return maximum of case1 and case2
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # memorize the result, calculate the size of max common sequence for s1 and s2
        # p1, p2: indexes of substring in text1 and text2
        @lru_cache(maxsize=None)
        def lcs_helper(p1: int, p2: int) -> int:
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # Case: first letter is not part of the optional solution
            # examples: s1 = [a, b, c, d, e, f], s2 = [b, c, d, a, e, f]
            # first letter of s1, is not part of the optimal solution
            # optimal Solution: [b, c, d, e, f]
            # if we pick a as the first letter, we will end up with [a, e, f]
            case1 = lcs_helper(p1 + 1, p2)

            # Case: first letter as path of the optimal solution
            letter1 = text1[p1]
            # firstOccurence = first position of letter1 in text2, from p2 position
            # find(sub, start, end) method will return -1, if not found
            first_occurence = text2.find(letter1, p2)
            case2 = 0
            if first_occurence != -1:
                case2 = 1 + lcs_helper(p1 + 1, first_occurence + 1)

            return max(case1, case2)

        return lcs_helper(0, 0)

# Optimized recursion, when 1st letter of 2 sequences are the same
class SolutionOptimizedRecursive:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)  # default maxsize=128
        def lcs_dp(p1: int, p2: int):
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # greedy when first letter is the same for both sequences
            if text1[p1] == text2[p2]:
                return 1 + lcs_dp(p1 + 1, p2 + 1)
            # two sequences does not have the same first letter
            else:
                # Case: first letter in p1 is a part of optimal solution
                case1 = lcs_dp(p1, p2 + 1)

                # Case: first letter in p1 is not a part of optimal Solution
                case2 = lcs_dp(p1 + 1, p2)
                return max(case1, case2)

        return lcs_dp(0, 0)
    
import pytest
import time

@pytest.fixture
def bottom_up_solution():
    return Solution()

@pytest.fixture
def unoptimized_recursive_solution():
    return SolutionUnoptimizeRecursive()

@pytest.fixture
def optimized_recursive_solution():
    return SolutionOptimizedRecursive()

@pytest.fixture
def all_solutions():
    return [Solution(), SolutionUnoptimizeRecursive(), SolutionOptimizedRecursive()]

# Test cases in format: (text1, text2, expected_output, description)
TEST_CASES = [
    # Examples from problem statement
    ("abcde", "ace", 3, "Example 1: Basic subsequence"),
    ("abc", "abc", 3, "Example 2: Identical strings"),
    ("abc", "def", 0, "Example 3: No common subsequence"),
    
    # Edge cases
    ("a", "a", 1, "Single character, matching"),
    ("a", "b", 0, "Single character, not matching"),
    ("", "abc", 0, "Empty first string"),
    ("abc", "", 0, "Empty second string"),
    ("", "", 0, "Both strings empty"),
    
    # Common scenarios
    ("abcdef", "acef", 4, "Multiple matching characters"),
    ("abcdef", "fedcba", 1, "Reversed strings"),
    ("aaaaaa", "aaa", 3, "Repeated characters"),
    ("abcabcabc", "abcabc", 6, "Repeating patterns"),
    
    # Complex cases
    ("bsbininm", "jmjkbkjkv", 1, "Sparse matches"),
    ("oxcpqrsvwf", "shmtulqrypy", 2, "Few matches in long strings"),
    ("mhunuzqrkzsnidwbun", "szulspmhwpazoxijwbq", 6, "Longer complex strings"),
    
    # Long identical sequences
    ("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", 26, "Long identical strings"),
    
    # Interleaved sequences
    ("abcdefg", "xaxbxcxdxexfxgx", 7, "Interleaved characters")
]

@pytest.mark.parametrize("text1, text2, expected, description", TEST_CASES)
def test_all_implementations(all_solutions, text1, text2, expected, description):
    """Test all three implementations with the test cases."""
    for solution in all_solutions:
        solution_name = solution.__class__.__name__
        result = solution.longestCommonSubsequence(text1, text2)
        assert result == expected, f"{solution_name} failed: {description}"

def test_solutions_equivalent():
    """Test that all solutions produce the same results for various inputs."""
    bottom_up = Solution()
    unoptimized = SolutionUnoptimizeRecursive()
    optimized = SolutionOptimizedRecursive()
    
    additional_test_cases = [
        ("pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopically"),
        ("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"),
        ("ababababababababababababab", "bababababababababababababa"),
        ("mississippi", "missouri"),
        ("technological", "terminology")
    ]
    
    for text1, text2 in additional_test_cases:
        bottom_up_result = bottom_up.longestCommonSubsequence(text1, text2)
        unoptimized_result = unoptimized.longestCommonSubsequence(text1, text2)
        optimized_result = optimized.longestCommonSubsequence(text1, text2)
        
        assert bottom_up_result == unoptimized_result == optimized_result, \
            f"Solutions gave different results for '{text1}' and '{text2}'"

def test_performance_comparison():
    """Compare performance of all three solutions with moderately sized inputs."""
    bottom_up = Solution()
    unoptimized = SolutionUnoptimizeRecursive()
    optimized = SolutionOptimizedRecursive()
    
    text1 = "abcdefghijklmnopqrstuvwxyz" * 3  # 78 characters
    text2 = "zyxwvutsrqponmlkjihgfedcba" * 3  # 78 characters
    
    # Time the bottom-up solution
    start_bu = time.time()
    result_bu = bottom_up.longestCommonSubsequence(text1, text2)
    end_bu = time.time()
    time_bu = end_bu - start_bu
    
    # Time the optimized recursive solution
    start_opt = time.time()
    result_opt = optimized.longestCommonSubsequence(text1, text2)
    end_opt = time.time()
    time_opt = end_opt - start_opt
    
    # Time the unoptimized recursive solution (may be slow)
    start_unopt = time.time()
    result_unopt = unoptimized.longestCommonSubsequence(text1, text2)
    end_unopt = time.time()
    time_unopt = end_unopt - start_unopt
    
    # Verify all solutions give the same result
    assert result_bu == result_opt == result_unopt
    
    # Check that all solutions complete in a reasonable time
    # (thresholds may need adjustment based on machine)
    assert time_bu < 1.0, f"Bottom-up solution too slow: {time_bu:.2f}s"
    assert time_opt < 1.0, f"Optimized recursive solution too slow: {time_opt:.2f}s"
    assert time_unopt < 2.0, f"Unoptimized recursive solution too slow: {time_unopt:.2f}s"

def test_large_input_bottom_up():
    """Test the bottom-up solution with large inputs (should handle efficiently)."""
    solution = Solution()
    
    # Create strings with length close to the constraint maximum (1000)
    text1 = "ab" * 499  # 998 characters
    text2 = "ba" * 499  # 998 characters
    
    start = time.time()
    result = solution.longestCommonSubsequence(text1, text2)
    end = time.time()
    
    # The expected result is 499 (every other character matches)
    assert result == 997
    assert (end - start) < 2.0, "Bottom-up solution took too long for large input"

def test_large_input_optimized_recursive():
    """Test the optimized recursive solution with large inputs."""
    solution = SolutionOptimizedRecursive()
    
    # Use moderately large strings that won't cause stack overflow
    text1 = "ab" * 200  # 400 characters
    text2 = "ba" * 200  # 400 characters
    
    start = time.time()
    result = solution.longestCommonSubsequence(text1, text2)
    end = time.time()
    
    assert result == 399
    assert (end - start) < 2.0, "Optimized recursive solution took too long"

def test_constraint_boundary():
    """Test with inputs at the boundary of the problem constraints."""
    solution = Solution()  # Using bottom-up as it should handle large inputs best
    
    # Create strings with exactly 1000 characters (max constraint)
    text1 = "a" * 1000
    text2 = "a" * 1000
    
    result = solution.longestCommonSubsequence(text1, text2)
    assert result == 1000, "Failed with maximum length identical strings"
    
    # Test with max length strings that have no common subsequence
    text1 = "a" * 1000
    text2 = "b" * 1000
    
    result = solution.longestCommonSubsequence(text1, text2)
    assert result == 0, "Failed with maximum length non-matching strings"

def test_special_patterns():
    """Test with special patterns that might challenge the algorithms."""
    all_solutions = [Solution(), SolutionOptimizedRecursive()]  # Skip unoptimized for speed
    
    # Pattern where naive approaches might be inefficient
    text1 = "aaaaaaaaaaaaaaaaaaaab"
    text2 = "aaaaaaaaaaaaaaaaaaaac"
    expected = 20  # All 'a's match
    
    for solution in all_solutions:
        solution_name = solution.__class__.__name__
        result = solution.longestCommonSubsequence(text1, text2)
        assert result == expected, f"{solution_name} failed with special pattern"