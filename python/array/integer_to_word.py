# https://leetcode.com/problems/integer-to-english-words/description/
"""
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1
"""
from collections import deque
import pytest

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        chunks = deque()
        temp = num
        dic = {
            1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
        }

        thousand_dic = {
            0: '', 1: 'Thousand', 2: 'Million', 3: 'Billion', 4: 'Trillion'
        }

        while temp > 0:
            modulo = temp % 1000
            chunks.append(modulo)
            temp = temp // 1000

        def get_word(input: int) -> str:
            s = []
            if input >= 100:
                remainder = input // 100
                s.append(dic[remainder] + ' Hundred')
                input %= 100

            if input > 0:
                if input in dic:
                    s.append(dic[input])
                else:
                    first = input // 10
                    rounded_first = first * 10
                    s.append(dic[rounded_first])
                    remainder = input % 10
                    if remainder != 0:
                        s.append(dic[remainder])
            return " ".join(s)

        output = []
        for i in range(len(chunks) - 1, -1, -1):
            chunk_val = chunks[i]
            if chunk_val != 0:
                words = get_word(chunk_val)
                if thousand_dic[i]:
                    words += " " + thousand_dic[i]
                output.append(words)

        return " ".join(output)
    
# === TEST CASES ===

@pytest.fixture
def solution():
    """Provides an instance of the Solution class."""
    return Solution()

def test_zero(solution):
    """Test with zero."""
    num = 0
    expected = "Zero"
    assert solution.numberToWords(num) == expected

def test_single_digit(solution):
    """Test with single digit numbers."""
    assert solution.numberToWords(1) == "One"
    assert solution.numberToWords(5) == "Five"
    assert solution.numberToWords(9) == "Nine"

def test_teens(solution):
    """Test with teen numbers."""
    assert solution.numberToWords(10) == "Ten"
    assert solution.numberToWords(11) == "Eleven"
    assert solution.numberToWords(15) == "Fifteen"
    assert solution.numberToWords(19) == "Nineteen"

def test_two_digits(solution):
    """Test with two digit numbers."""
    assert solution.numberToWords(20) == "Twenty"
    assert solution.numberToWords(45) == "Forty Five"
    assert solution.numberToWords(99) == "Ninety Nine"

def test_three_digits(solution):
    """Test with three digit numbers."""
    assert solution.numberToWords(100) == "One Hundred"
    assert solution.numberToWords(101) == "One Hundred One"
    assert solution.numberToWords(110) == "One Hundred Ten"
    assert solution.numberToWords(123) == "One Hundred Twenty Three"
    assert solution.numberToWords(999) == "Nine Hundred Ninety Nine"

def test_examples(solution):
    """Test the examples from the problem description."""
    assert solution.numberToWords(123) == "One Hundred Twenty Three"
    assert solution.numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five"
    assert solution.numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

def test_thousands(solution):
    """Test with thousands."""
    assert solution.numberToWords(1000) == "One Thousand"
    assert solution.numberToWords(1001) == "One Thousand One"
    assert solution.numberToWords(1234) == "One Thousand Two Hundred Thirty Four"
    assert solution.numberToWords(9999) == "Nine Thousand Nine Hundred Ninety Nine"

def test_millions(solution):
    """Test with millions."""
    assert solution.numberToWords(1000000) == "One Million"
    assert solution.numberToWords(1000001) == "One Million One"
    assert solution.numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    assert solution.numberToWords(999999999) == "Nine Hundred Ninety Nine Million Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine"

def test_billions(solution):
    """Test with billions."""
    assert solution.numberToWords(1000000000) == "One Billion"
    assert solution.numberToWords(2000000001) == "Two Billion One"
    assert solution.numberToWords(1234567890) == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety"
    assert solution.numberToWords(2147483647) == "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"  # Max 32-bit signed int

def test_zeros_in_different_places(solution):
    """Test with zeros in different places."""
    assert solution.numberToWords(101) == "One Hundred One"
    assert solution.numberToWords(1001) == "One Thousand One"
    assert solution.numberToWords(10001) == "Ten Thousand One"
    assert solution.numberToWords(100001) == "One Hundred Thousand One"
    assert solution.numberToWords(1000001) == "One Million One"
    assert solution.numberToWords(10000001) == "Ten Million One"
    assert solution.numberToWords(100000001) == "One Hundred Million One"
    assert solution.numberToWords(1000000001) == "One Billion One"

def test_max_value(solution):
    """Test with value at the constraint limit."""
    max_int = 2**31 - 1  # 2,147,483,647
    expected = "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"
    assert solution.numberToWords(max_int) == expected

def test_round_numbers(solution):
    """Test with round numbers."""
    assert solution.numberToWords(20) == "Twenty"
    assert solution.numberToWords(300) == "Three Hundred"
    assert solution.numberToWords(4000) == "Four Thousand"
    assert solution.numberToWords(50000) == "Fifty Thousand"
    assert solution.numberToWords(600000) == "Six Hundred Thousand"
    assert solution.numberToWords(7000000) == "Seven Million"
    assert solution.numberToWords(80000000) == "Eighty Million"
    assert solution.numberToWords(900000000) == "Nine Hundred Million"
    assert solution.numberToWords(1000000000) == "One Billion"

def test_consecutive_zeros(solution):
    """Test with consecutive zeros in the number."""
    assert solution.numberToWords(10000) == "Ten Thousand"
    assert solution.numberToWords(100000) == "One Hundred Thousand"
    assert solution.numberToWords(1000000) == "One Million"
    assert solution.numberToWords(1000100) == "One Million One Hundred"
    assert solution.numberToWords(1001000) == "One Million One Thousand"
    assert solution.numberToWords(1001001) == "One Million One Thousand One"