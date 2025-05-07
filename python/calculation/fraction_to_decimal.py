# Step-by-step long division for 4 / 333
# We track remainders to detect cycles

# | Step | Remainder | Multiply by 10 | remainder // 333 | New Remainder | Fraction | Lookup Map          |
# |------|-----------|----------------|------------------|---------------|----------|---------------------|
# | 0    | 4         | 40             | 0                | 40            | 0.0      | store 4 → pos 2     |
# | 1    | 40        | 400            | 1                | 67            | 0.01     | store 40 → pos 3    |
# | 2    | 67        | 670            | 2                | 4             | 0.012    | store 67 → pos 4    |
# | 3    | 4         | cycle detected |                  |               | 0.(012)  | repeat starts at 2  |
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # case1: Numerator is zero.
        # case2: (20/4) answer is a whole integer, remove the fractional part
        # case3: (1/2), answer is 0.5, no recurring decimal.
        # case4: one of numerator or denominator is negative. Append negative to result
        # case5: both numerator and denominator is negative. No appending of - sign
        if numerator == 0:
            return "0"
        result = []
        if (numerator < 0) != (denominator < 0):
            result.append('-')
        dividend = abs(numerator)
        divisor = abs(denominator)

        # Append the integer part
        result.append(str(dividend // divisor))
        remainder = dividend % divisor
        if remainder == 0:
            return "".join(result)

        # Begin processing decimal part
        result.append(".")
        remainder_map = {}  # map from remainder to index position in the result
        while remainder != 0:
            if remainder in remainder_map:
                # insert ( into the index of remainder, shift remainder 1 step right-side
                result.insert(remainder_map[remainder], "(")
                result.append(")")
                break

            # memorize the position of this remainder
            remainder_map[remainder] = len(result)

            remainder *= 10
            result.append(str(remainder // divisor))
            remainder %= divisor
        return "".join(result)
    

# === TEST CASES ===

import pytest  # noqa: E402
# from typing import List # Not used in the solution directly, but good practice

@pytest.fixture
def solution_instance():
    return Solution()

def test_numerator_zero(solution_instance):
    assert solution_instance.fractionToDecimal(0, 1) == "0"
    assert solution_instance.fractionToDecimal(0, -5) == "0"
    assert solution_instance.fractionToDecimal(0, 100) == "0"

def test_whole_number_result(solution_instance):
    assert solution_instance.fractionToDecimal(4, 2) == "2"
    assert solution_instance.fractionToDecimal(20, 4) == "5"
    assert solution_instance.fractionToDecimal(100, 10) == "10"
    assert solution_instance.fractionToDecimal(-6, 3) == "-2"
    assert solution_instance.fractionToDecimal(6, -3) == "-2"
    assert solution_instance.fractionToDecimal(-6, -3) == "2"

def test_terminating_decimal(solution_instance):
    assert solution_instance.fractionToDecimal(1, 2) == "0.5"
    assert solution_instance.fractionToDecimal(2, 5) == "0.4"
    assert solution_instance.fractionToDecimal(5, 8) == "0.625" # 5/8 = 0.625
    assert solution_instance.fractionToDecimal(1, 4) == "0.25"
    assert solution_instance.fractionToDecimal(3, 4) == "0.75"
    assert solution_instance.fractionToDecimal(1, 10) == "0.1"
    assert solution_instance.fractionToDecimal(1, 100) == "0.01"
    assert solution_instance.fractionToDecimal(123, 1000) == "0.123"

def test_terminating_decimal_negative(solution_instance):
    assert solution_instance.fractionToDecimal(-1, 2) == "-0.5"
    assert solution_instance.fractionToDecimal(1, -2) == "-0.5"
    assert solution_instance.fractionToDecimal(-1, -2) == "0.5"
    assert solution_instance.fractionToDecimal(-5, 8) == "-0.625"

def test_recurring_decimal_simple(solution_instance):
    assert solution_instance.fractionToDecimal(1, 3) == "0.(3)"
    assert solution_instance.fractionToDecimal(2, 3) == "0.(6)"
    assert solution_instance.fractionToDecimal(1, 6) == "0.1(6)" # 1/6 = 0.1666...
    assert solution_instance.fractionToDecimal(1, 7) == "0.(142857)" # 1/7
    assert solution_instance.fractionToDecimal(22, 7) == "3.(142857)" # Pi approximation

def test_recurring_decimal_negative(solution_instance):
    assert solution_instance.fractionToDecimal(-1, 3) == "-0.(3)"
    assert solution_instance.fractionToDecimal(1, -3) == "-0.(3)"
    assert solution_instance.fractionToDecimal(-1, -3) == "0.(3)"
    assert solution_instance.fractionToDecimal(-1, 6) == "-0.1(6)"

def test_recurring_decimal_complex(solution_instance):
    assert solution_instance.fractionToDecimal(4, 333) == "0.(012)"
    assert solution_instance.fractionToDecimal(1, 90) == "0.0(1)" # 1/90 = 0.0111...
    assert solution_instance.fractionToDecimal(1, 99) == "0.(01)"
    assert solution_instance.fractionToDecimal(1, 999) == "0.(001)"
    assert solution_instance.fractionToDecimal(1, 11) == "0.(09)"
    assert solution_instance.fractionToDecimal(1, 13) == "0.(076923)"

def test_numerator_larger_than_denominator_recurring(solution_instance):
    assert solution_instance.fractionToDecimal(7, 3) == "2.(3)" # 7/3 = 2.333...
    assert solution_instance.fractionToDecimal(10, 6) == "1.(6)" # 10/6 = 5/3 = 1.666...
    assert solution_instance.fractionToDecimal(50, 22) == "2.(27)" # 50/22 = 25/11 = 2.2727...

def test_numerator_larger_than_denominator_terminating(solution_instance):
    assert solution_instance.fractionToDecimal(5, 2) == "2.5"
    assert solution_instance.fractionToDecimal(10, 4) == "2.5"
    assert solution_instance.fractionToDecimal(7, 5) == "1.4"

def test_edge_cases_from_leetcode(solution_instance):
    assert solution_instance.fractionToDecimal(1, 2) == "0.5"
    assert solution_instance.fractionToDecimal(2, 1) == "2"
    assert solution_instance.fractionToDecimal(2, 3) == "0.(6)"
    assert solution_instance.fractionToDecimal(4, 333) == "0.(012)"
    assert solution_instance.fractionToDecimal(1, 5) == "0.2"
    assert solution_instance.fractionToDecimal(1, 90) == "0.0(1)"

def test_large_numbers_terminating(solution_instance):
    assert solution_instance.fractionToDecimal(1000, 8) == "125" # 1000/8 = 125
    assert solution_instance.fractionToDecimal(12345, 100) == "123.45"

def test_large_numbers_recurring(solution_instance):
    # This might be slow if the cycle is very long, but the logic should hold
    # Example: 1 / 9999999 (long cycle of 9s)
    # For testing, let's use a known shorter one with larger numbers
    assert solution_instance.fractionToDecimal(100, 33) == "3.(03)" # 100/33 = 3.0303...

def test_min_max_values_from_constraints_if_applicable(solution_instance):
    # Constraints: -2^31 <= numerator, denominator <= 2^31 - 1, denominator != 0
    # Python handles large integers, so overflow isn't an issue for the numbers themselves.
    # The length of the result string could be an issue for extremely long cycles,
    # but the algorithm's correctness for typical cycles should be testable.

    # Test with a value that might cause issues if not handled by abs() correctly
    INT_MIN = -2**31

    assert solution_instance.fractionToDecimal(INT_MIN, 1) == str(INT_MIN) # e.g. "-2147483648"
    assert solution_instance.fractionToDecimal(INT_MIN, -1) == str(abs(INT_MIN)) # e.g. "2147483648"
    # For INT_MIN / -1, abs(INT_MIN) can be larger than INT_MAX if INT_MIN is -2^31.
    # Python handles this fine.

    # A tricky case: -2147483648 / -1 = 2147483648
    # abs(numerator) = 2147483648, abs(denominator) = 1
    # result = "2147483648"
    assert solution_instance.fractionToDecimal(-2147483648, -1) == "2147483648"

    # Test with denominator that could lead to long non-repeating then repeating part
    # e.g., 1 / (2^k * 3^m)
    assert solution_instance.fractionToDecimal(1, 24) == "0.041(6)" # 1 / (8 * 3) = 0.041666...

    # Test with a case where remainder becomes 0 after some steps
    assert solution_instance.fractionToDecimal(1, 8) == "0.125"

    # Test a case that was problematic in some solutions if not careful
    assert solution_instance.fractionToDecimal(1, 17) == "0.(0588235294117647)"

# To run these tests (if they were in a separate file like test_fraction_to_decimal.py):
# 1. Make sure pytest is installed: pip install pytest
# 2. Navigate to the directory containing the test file and the solution file.
# 3. Run pytest in the terminal: pytest