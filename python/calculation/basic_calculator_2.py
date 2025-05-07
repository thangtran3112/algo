# https://leetcode.com/problems/basic-calculator-ii/description/
"""
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""
from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_num = 0
        prev_op = '+'

        # add '+' to the end of string s, so in the final interation
        # the loop will wrap up the curr_num
        for ch in s + '+':
            if ch == ' ':
                continue
            if ch.isdigit():
                curr_num = (curr_num * 10) + int(ch)
                continue

            # when we meet an operator
            if prev_op == '-':
                stack.append(-curr_num)
            elif prev_op == '+':
                stack.append(curr_num)
            elif prev_op == '*':
                top = stack.pop()
                stack.append(top * curr_num)
            elif prev_op == '/':
                top = stack.pop()
                stack.append(int(top / curr_num))
            curr_num = 0
            prev_op = ch

        return sum(stack)

class SolutionUnoptimized:
    # 3 + (2 * 2) - (3 / 2 / 4 * 9)
    # going from the end, put both number and operator in a stack
    # only adding to the stack when we meet * or /
    # if we meet + or -, we calculate the temp stack immediately
    def calculate(self, s: str) -> int:
        # (3 / 2 / 4 * 9) , when navigating from the end of the string
        # stack [9, *, 4, /, 2, / 3] and we pop from 3 -> 2 -> 4 -> 9
        def mutiplyOrDivide(stack: List[str]):
            if len(stack) == 0:
                return 0
            result = int(stack.pop())
            while stack:
                ops = stack.pop()
                y = stack.pop()
                if ops == '*':
                    result *= int(y)
                else:
                    result = result // int(y)
            return result

        arr = []
        result = 0
        i = len(s) - 1
        while i >= 0:
            letter = s[i]
            if letter == ' ':
                i -= 1
            elif letter == '+':
                result += mutiplyOrDivide(arr)
                arr = []
                i -= 1
            elif letter == '-':
                result -= mutiplyOrDivide(arr)
                arr = []
                i -= 1
            elif letter == '*' or letter == '/':
                arr.append(letter)
                i -= 1
            else:
                # letter is not an operator + or -, but it could be a multi-letter number
                # Eg: 423
                val = ''
                while i >= 0 and s[i] not in {' ', '+', '-', '*', '/'}:
                    val += s[i]
                    i -= 1
                reversed_val = ''.join(reversed(val))
                arr.append(reversed_val)

        return result + mutiplyOrDivide(arr) if len(arr) > 0 else result


## TEST CASES
import pytest  # noqa: E402


@pytest.fixture(params=[Solution, SolutionUnoptimized], ids=["Optimized", "Unoptimized"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    s = "3+2*2"
    expected = 7
    assert solution_instance.calculate(s) == expected

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    s = " 3/2 "
    expected = 1
    assert solution_instance.calculate(s) == expected

def test_example3(solution_instance):
    """Test Example 3 from the problem description."""
    s = " 3+5 / 2 "
    expected = 5
    assert solution_instance.calculate(s) == expected

def test_simple_addition(solution_instance):
    """Test simple addition."""
    s = "1+1"
    expected = 2
    assert solution_instance.calculate(s) == expected

def test_simple_subtraction(solution_instance):
    """Test simple subtraction."""
    s = "5-3"
    expected = 2
    assert solution_instance.calculate(s) == expected

def test_simple_multiplication(solution_instance):
    """Test simple multiplication."""
    s = "2*3"
    expected = 6
    assert solution_instance.calculate(s) == expected

def test_simple_division(solution_instance):
    """Test simple division."""
    s = "10/2"
    expected = 5
    assert solution_instance.calculate(s) == expected

def test_division_truncation(solution_instance):
    """Test that division truncates toward zero."""
    s = "7/3"
    expected = 2  # Truncated from 2.33...
    assert solution_instance.calculate(s) == expected

def test_multi_digit_numbers(solution_instance):
    """Test expressions with multi-digit numbers."""
    s = "123+456"
    expected = 579
    assert solution_instance.calculate(s) == expected

def test_whitespace_handling(solution_instance):
    """Test handling of whitespace."""
    s = "  1  +  2  *  3  "
    expected = 7
    assert solution_instance.calculate(s) == expected

def test_multiple_operations(solution_instance):
    """Test expression with multiple operations."""
    s = "2+3*4-6/3"
    expected = 12
    assert solution_instance.calculate(s) == expected

def test_precedence_of_operations(solution_instance):
    """Test that multiplication and division have precedence over addition and subtraction."""
    s = "1+2*3+4/2"
    expected = 9
    assert solution_instance.calculate(s) == expected

def test_consecutive_operations(solution_instance):
    """Test consecutive operations of the same type."""
    s = "2*3*4"
    expected = 24
    assert solution_instance.calculate(s) == expected

def test_complex_expression(solution_instance):
    """Test a more complex expression."""
    s = "10+20*30-40/5+60"
    expected = 10 + 20*30 - 40//5 + 60
    assert solution_instance.calculate(s) == expected

def test_large_numbers(solution_instance):
    """Test with large numbers within constraints."""
    s = "1000000000+1000000000*2"
    expected = 3000000000
    assert solution_instance.calculate(s) == expected

def test_no_spaces(solution_instance):
    """Test expression without any spaces."""
    s = "1+2*3-4/2"
    expected = 5
    assert solution_instance.calculate(s) == expected

def test_many_spaces(solution_instance):
    """Test expression with many spaces."""
    s = "   1   +   2   *   3   -   4   /   2   "
    expected = 5
    assert solution_instance.calculate(s) == expected

def test_consecutive_divisions(solution_instance):
    """Test consecutive division operations."""
    s = "100/5/2"
    expected = 10
    assert solution_instance.calculate(s) == expected

def test_single_number(solution_instance):
    """Test input with just a single number."""
    s = "42"
    expected = 42
    assert solution_instance.calculate(s) == expected

def test_division_by_one(solution_instance):
    """Test division by one."""
    s = "10/1"
    expected = 10
    assert solution_instance.calculate(s) == expected

def test_multiplication_by_one(solution_instance):
    """Test multiplication by one."""
    s = "10*1"
    expected = 10
    assert solution_instance.calculate(s) == expected

def test_alternating_operations(solution_instance):
    """Test alternating operations."""
    s = "1+2-3+4-5"
    expected = -1
    assert solution_instance.calculate(s) == expected

def test_multiplication_and_division_precedence(solution_instance):
    """Test that multiplication and division are evaluated from left to right."""
    s = "2*3/2"
    expected = 3
    assert solution_instance.calculate(s) == expected

def test_division_and_multiplication_precedence(solution_instance):
    """Test that division and multiplication are evaluated from left to right."""
    s = "6/3*2"
    expected = 4
    assert solution_instance.calculate(s) == expected