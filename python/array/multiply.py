# https://leetcode.com/problems/multiply-strings/description/
"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        len1 = len(num1)
        len2 = len(num2)
        total_len = len1 + len2

        # the final product in term of digits.
        # The result of m digits * n digits would result in maximum m + n digits
        # eg: 123 * 45 = 5535
        product = [0] * total_len

        # illustrations of 45 * 123
        #         1 5           5 * 3
        #       1 2             4 * 3
        #       1 0             5 * 2
        #       8               4 * 2
        #       5               5 * 1
        #     4                 4 * 1
        #     5 5 3 5
        # Eg. outer loop round 1
        for i in range(len1 - 1, -1, -1):
            a = int(num1[i])  # a = 3
            for j in range(len2 - 1, -1, -1):
                b = int(num2[j])  # inner loop (round 1,b = 5), (round 2, b = 4)
                idx = i + j + 1
                p = a * b + product[idx]
                product[idx] = p % 10
                product[idx - 1] += p // 10
            # after first innter loop, product = [0, 0, 0, 1, 5]
            # after second inner loop, product = [0, 0, 1, 3, 5] as 45 * 3

        # first element in product array could be 0
        start = 0 if product[0] != 0 else 1
        result = ""
        while start < total_len:
            result += str(product[start])
            start += 1

        return result
    
        # === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture
def solution():
    """Fixture to provide a Solution instance."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description."""
    num1 = "2"
    num2 = "3"
    assert solution.multiply(num1, num2) == "6"

def test_example2(solution):
    """Test Example 2 from the problem description."""
    num1 = "123"
    num2 = "456"
    assert solution.multiply(num1, num2) == "56088"

def test_multiply_by_zero(solution):
    """Test multiplication by zero."""
    num1 = "123"
    num2 = "0"
    assert solution.multiply(num1, num2) == "0"
    
    num1 = "0"
    num2 = "456"
    assert solution.multiply(num1, num2) == "0"
    
    num1 = "0"
    num2 = "0"
    assert solution.multiply(num1, num2) == "0"

def test_single_digits(solution):
    """Test multiplication of single digits."""
    for i in range(1, 10):
        for j in range(1, 10):
            num1 = str(i)
            num2 = str(j)
            expected = str(i * j)
            assert solution.multiply(num1, num2) == expected

def test_multiply_by_one(solution):
    """Test multiplication by one."""
    num1 = "12345"
    num2 = "1"
    assert solution.multiply(num1, num2) == num1

def test_larger_numbers(solution):
    """Test multiplication of larger numbers."""
    num1 = "9999"
    num2 = "9999"
    assert solution.multiply(num1, num2) == "99980001"

def test_specific_example(solution):
    """Test specific example shown in the code comments."""
    num1 = "123"
    num2 = "45"
    assert solution.multiply(num1, num2) == "5535"

def test_max_length_constraints(solution):
    """Test with numbers at the maximum allowed length."""
    # Create two 200-digit numbers
    num1 = "1" + "0" * 199  # 1 followed by 199 zeros
    num2 = "2"
    expected = "2" + "0" * 199  # 2 followed by 199 zeros
    assert solution.multiply(num1, num2) == expected

def test_powers_of_ten(solution):
    """Test multiplication with powers of ten."""
    num1 = "10"
    num2 = "10"
    assert solution.multiply(num1, num2) == "100"
    
    num1 = "100"
    num2 = "100"
    assert solution.multiply(num1, num2) == "10000"

def test_commutative_property(solution):
    """Test the commutative property of multiplication."""
    num1 = "123"
    num2 = "456"
    assert solution.multiply(num1, num2) == solution.multiply(num2, num1)

def test_associative_property(solution):
    """Test the associative property using string multiplication."""
    # (2 * 3) * 4 = 2 * (3 * 4)
    result1 = solution.multiply(solution.multiply("2", "3"), "4")
    result2 = solution.multiply("2", solution.multiply("3", "4"))
    assert result1 == result2 == "24"