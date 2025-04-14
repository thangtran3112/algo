# https://leetcode.com/problems/happy-number/description/
"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
"""
class SolutionHashset:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                # Loop detected
                return False
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return True

class ListNode:
    def __init__(self, val: int):
        self.val = val

    def next(self):
        nextVal = sum(int(digit) ** 2 for digit in str(self.val))
        return ListNode(nextVal)

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = ListNode(n)
        fast = ListNode(n)

        while fast.val != 1:
            if fast.next().val != 1:
                fast = fast.next()
                if slow.val == fast.val:
                    # loop detected
                    return False
            slow = slow.next()
            fast = fast.next()
        return True

# TEST CASES
import pytest  # noqa: E402

@pytest.fixture(params=[SolutionHashset, Solution])
def solution(request):
    """Fixture that provides both solution implementations."""
    return request.param()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    # n = 19 should be a happy number
    assert solution.isHappy(19) is True

def test_example_2(solution):
    """Test the second example from the problem statement."""
    # n = 2 should not be a happy number
    assert solution.isHappy(2) is False

def test_one(solution):
    """Test with n = 1."""
    # 1 is already a happy number by definition
    assert solution.isHappy(1) is True

def test_known_happy_numbers(solution):
    """Test with several known happy numbers."""
    happy_numbers = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]
    for num in happy_numbers:
        assert solution.isHappy(num) is True

def test_known_unhappy_numbers(solution):
    """Test with several known unhappy numbers."""
    unhappy_numbers = [2, 3, 4, 5, 6, 8, 9, 11, 12, 14, 15, 16, 17, 18, 20]
    for num in unhappy_numbers:
        assert solution.isHappy(num) is False

def test_larger_numbers(solution):
    """Test with larger numbers."""
    # 7 is a happy number
    assert solution.isHappy(7) is True
    # 1111111 (7 ones) is a happy number
    assert solution.isHappy(1111111) is True
    # 9999999 (7 nines) is not a happy number
    assert solution.isHappy(9999999) is False

def test_sequence(solution):
    """Test a specific sequence that's known to lead to 1."""
    # Starting with 19:
    # 19 -> 82 -> 68 -> 100 -> 1
    
    # To verify internal logic for SolutionHashset
    if isinstance(solution, SolutionHashset):
        n = 19
        seen = set()
        
        while n != 1:
            if n in seen:
                assert False, f"Unexpected cycle detected at {n}"
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
            
            # Verify we're seeing the expected sequence
            if 19 in seen and n not in [82, 68, 100, 1]:
                assert False, f"Unexpected value {n} in the sequence"
        
        assert n == 1
    
    # The actual test
    assert solution.isHappy(19) is True

def test_multiple_digit_squares(solution):
    """Test that the solution correctly handles multiple digit squares."""
    # For 1000:
    # 1^2 + 0^2 + 0^2 + 0^2 = 1 -> happy number
    assert solution.isHappy(1000) is True

def test_cycle_detection(solution):
    """Test that the solution correctly detects cycles."""
    # For n=2, the sequence is:
    # 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 (cycle detected)
    assert solution.isHappy(2) is False

def test_performance_with_long_chains(solution):
    """Test performance with numbers that have long chains before becoming 1 or cycling."""
    # This number has a longer chain before becoming 1
    assert solution.isHappy(28) is True
    
    # This number has a longer chain before cycling
    assert solution.isHappy(37) is False