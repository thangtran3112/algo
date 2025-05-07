# https://leetcode.com/problems/strobogrammatic-number-ii/description/
"""
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:

Input: n = 2
Output: ["11","69","88","96"]
Example 2:

Input: n = 1
Output: ["0","1","8"]
 

Constraints:

1 <= n <= 14
"""

from collections import defaultdict
from typing import List
import pytest

class SolutionRecursive:
    def findStrobogrammatic(self, n: int) -> List[str]:
        """
        * At n, the result is built upon n - 2
        * If we build from the center of each element in result[n - 2]
        * "1" + element + "1" will also remain the same strobogramatic number
        """
        def build(m: int) -> List[str]:
            if m == 0:
                return [""]
            if m == 1:
                return ["0", "1", "8"]

            middles = build(m - 2)
            result = []

            for middle in middles:
                for a, b in [("0", "0"), ("1", "1"), ("6", "9"), ("9", "6"), ("8", "8")]:
                    # Skip numbers that start with '0' unless it's the outermost layer of a 1-digit number
                    if m != n or a != "0":
                        result.append(a + middle + b)
            return result

        return build(n)

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        dp = defaultdict(list)
        dp[0] = [""]
        dp[1] = ["0", "1", "8"]
        if n <= 1:
            return dp[n]
        possible_edges = [("0", "0"), ("1", "1"), ("6", "9"), ("9", "6"), ("8", "8")]

        for i in range(2, n + 1):
            for middle in dp[i - 2]:
                for a, b in possible_edges:
                    dp[i].append(a + middle + b)

        # Notes: we need to use ("0","0") for any dp[k] when k != n
        # Eg. we could build "1001", but using dp[2] = ["00", "11", "69", "96", "88"]
        # dp[4] = ["1001", "6009", "8008", ...]
        # filter out any number with leading zero for the final result, such as "0690"

        result = []
        for value in dp[n]:
            if value[0] != "0":
                result.append(value)
        return result
    
# === TEST CASES ===

# Assuming SolutionRecursive and Solution are defined above in the same file.

# Helper to sort the list of strings for comparison, as order doesn't matter.
def normalize_results(results: List[str]) -> List[str]:
    return sorted(results)

@pytest.fixture(params=[SolutionRecursive, Solution], ids=["Recursive", "DP"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_n1(solution_instance):
    """Test with n = 1."""
    n = 1
    expected = ["0", "1", "8"]
    result = solution_instance.findStrobogrammatic(n)
    assert normalize_results(result) == normalize_results(expected)

def test_n2(solution_instance):
    """Test with n = 2."""
    n = 2
    expected = ["11", "69", "88", "96"]
    result = solution_instance.findStrobogrammatic(n)
    assert normalize_results(result) == normalize_results(expected)

def test_n3(solution_instance):
    """Test with n = 3."""
    n = 3
    expected = [
        "101", "111", "181",
        "609", "619", "689",
        "808", "818", "888",
        "906", "916", "986"
    ]
    result = solution_instance.findStrobogrammatic(n)
    assert normalize_results(result) == normalize_results(expected)

def test_n4(solution_instance):
    """Test with n = 4."""
    n = 4
    expected = [
        "1001", "1111", "1691", "1881", "1961",
        "6009", "6119", "6699", "6889", "6969",
        "8008", "8118", "8698", "8888", "8968",
        "9006", "9116", "9696", "9886", "9966"
    ]
    result = solution_instance.findStrobogrammatic(n)
    assert normalize_results(result) == normalize_results(expected)