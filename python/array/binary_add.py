# https://leetcode.com/problems/add-binary/description/
"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        builder = []
        # doing the summation in reversed way
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            builder.append(str(carry % 2))
            if carry >= 2:
                carry = 1
            else:
                carry = 0
        if carry == 1:
            builder.append('1')
        # result is not a string, it is char array, ['1', '0', '1']
        return ''.join(reversed(builder))

class SolutionConversion:
    def addBinary(self, a: str, b: str) -> str:
        def convert(x: str) -> int:
            sequences = [int(digit) for digit in x]
            sequences.reverse()
            val = 0
            for i in range(len(sequences)):
                val += sequences[i] * (2 ** i)
            return val

        def toBinary(x: int) -> str:
            if x == 0:
                return '0'
            result = []
            # eg 7: 7 % 2 = 1, 3 % 2 = 1, 1 % 2 = 1. Result = 111
            # eg 11: 1011
            while x > 0:
                result.append(x % 2)
                x = x // 2
            # result is now an array of number [1, 0, 0]
            s = ''
            for digit in reversed(result):
                s += str(digit)
            return s

        a_val = convert(a)
        b_val = convert(b)

        return toBinary(a_val + b_val)

import pytest  # noqa: E402

@pytest.fixture(params=[Solution, SolutionConversion])
def solution(request):
    """Fixture that provides both solution implementations."""
    return request.param()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    a = "11"
    b = "1"
    assert solution.addBinary(a, b) == "100"

def test_example_2(solution):
    """Test the second example from the problem statement."""
    a = "1010"
    b = "1011"
    assert solution.addBinary(a, b) == "10101"

def test_same_length_strings(solution):
    """Test with binary strings of the same length."""
    a = "1111"
    b = "1111"
    assert solution.addBinary(a, b) == "11110"

def test_different_length_strings(solution):
    """Test with binary strings of different lengths."""
    a = "11111"
    b = "1"
    assert solution.addBinary(a, b) == "100000"

def test_zero_plus_zero(solution):
    """Test adding zero to zero."""
    assert solution.addBinary("0", "0") == "0"

def test_zero_plus_one(solution):
    """Test adding zero to one."""
    assert solution.addBinary("0", "1") == "1"
    assert solution.addBinary("1", "0") == "1"

def test_multiple_carries(solution):
    """Test scenario with multiple carries."""
    assert solution.addBinary("1111", "1") == "10000"
    
def test_very_long_strings(solution):
    """Test with very long binary strings."""
    a = "1" * 100  # 100 ones
    b = "1"
    # Expected result: 1 followed by 100 zeros
    expected = "1" + "0" * 100
    assert solution.addBinary(a, b) == expected

def test_alternating_bits(solution):
    """Test with alternating bit patterns."""
    assert solution.addBinary("10101", "01010") == "11111"
    
def test_single_bit(solution):
    """Test with single-bit inputs."""
    assert solution.addBinary("1", "1") == "10"

def test_only_one_has_value(solution):
    """Test when one string has value and other is zero."""
    assert solution.addBinary("1010", "0") == "1010"
    assert solution.addBinary("0", "1010") == "1010"

def test_complex_addition(solution):
    """Test more complex binary addition scenarios."""
    assert solution.addBinary("110110", "10111") == "1001101"
    assert solution.addBinary("1100100", "110101") == "10011001"
