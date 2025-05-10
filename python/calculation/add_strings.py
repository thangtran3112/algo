# https://leetcode.com/problems/add-strings
"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def get_digit(ch: str):
            return ord(ch) - ord('0')
        carry = 0
        sb = []
        first = len(num1) - 1
        second = len(num2) - 1
        while first >= 0 or second >= 0:
            # cases that one of the two strings has finished processing
            first_digit = num1[first] if first >= 0 else "0"
            second_digit = num2[second] if second >= 0 else "0"
            curr_total = get_digit(first_digit) + get_digit(second_digit) + carry
            sb.append(str(curr_total % 10))
            carry = 1 if curr_total >= 10 else 0
            first -= 1
            second -= 1
        if carry == 1:
            sb.append("1")
        # result will contains all digits str in final result, but in reversed order
        sb.reverse()
        return "".join(sb)
    
import pytest  # noqa: E402

@pytest.fixture
def solution_instance():
    return Solution()

def test_example1(solution_instance):
    """Input: num1 = "11", num2 = "123" -> Output: "134"""
    num1 = "11"
    num2 = "123"
    assert solution_instance.addStrings(num1, num2) == "134"

def test_example2(solution_instance):
    """Input: num1 = "456", num2 = "77" -> Output: "533"""
    num1 = "456"
    num2 = "77"
    assert solution_instance.addStrings(num1, num2) == "533"

def test_example3(solution_instance):
    """Input: num1 = "0", num2 = "0" -> Output: "0"""
    num1 = "0"
    num2 = "0"
    assert solution_instance.addStrings(num1, num2) == "0"

def test_single_digit_addition(solution_instance):
    """Test adding single digits."""
    num1 = "5"
    num2 = "7"
    assert solution_instance.addStrings(num1, num2) == "12"

def test_carrying_over(solution_instance):
    """Test carrying over in addition."""
    num1 = "999"
    num2 = "1"
    assert solution_instance.addStrings(num1, num2) == "1000"

def test_different_lengths(solution_instance):
    """Test adding numbers of different lengths."""
    num1 = "1234567890"
    num2 = "9876"
    assert solution_instance.addStrings(num1, num2) == "1234577766"

def test_zero_plus_number(solution_instance):
    """Test adding zero to a number."""
    num1 = "0"
    num2 = "123456789"
    assert solution_instance.addStrings(num1, num2) == "123456789"

def test_large_numbers(solution_instance):
    """Test adding very large numbers."""
    num1 = "9" * 10000  # 10000 nines
    num2 = "1"
    assert solution_instance.addStrings(num1, num2) == "1" + "0" * 10000

def test_same_number(solution_instance):
    """Test adding a number to itself."""
    num1 = "12345"
    num2 = "12345"
    assert solution_instance.addStrings(num1, num2) == "24690"

# To run these tests:
# 1. Make sure pytest is installed: pip install pytest
# 2. Navigate to the directory containing the test file and the solution file.
# 3. Run pytest in the terminal: pytest test_add_strings.py