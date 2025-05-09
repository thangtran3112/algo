# https://leetcode.com/problems/valid-number/description/
"""
Given a string s, return whether s is a valid number.

For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

Formally, a valid number is defined using one of the following definitions:

An integer number followed by an optional exponent.
A decimal number followed by an optional exponent.
An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

Digits followed by a dot '.'.
Digits followed by a dot '.' followed by digits.
A dot '.' followed by digits.
An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.

 

Example 1:

Input: s = "0"

Output: true

Example 2:

Input: s = "e"

Output: false

Example 3:

Input: s = "."

Output: false

 

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""
class SolutionNatural:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot = False
        s = s.lower()
        # so we do not need deal with E and e cases
        for i, ch in enumerate(s.lower()):
            if ch.isdigit():
                seen_digit = True
            elif ch in {"+", "-"}:
                # +/- sign can only be at beginning or after e exponential
                if i > 0 and s[i - 1] != 'e':
                    return False
            elif ch == 'e':
                # there has been e before, or there is no digit previously
                # "e3", "1e", "90ee"
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif ch == '.':
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                # unrecognized letter
                return False
        return seen_digit

# DFA solution wtih state machine
class SolutionStateMachine:
    def isNumber(self, s: str) -> bool:
        # This is the DFA we have designed above
        dfa = [
            {"digit": 1, "sign": 2, "dot": 3},  # state 0
            {"digit": 1, "dot": 4, "exponent": 5},  # state 1
            {"digit": 1, "dot": 3},  # state 2
            {"digit": 4},  # state 3
            {"digit": 4, "exponent": 5},  # state 4
            {"sign": 6, "digit": 7},  # state 5
            {"digit": 7},  # state 6
            {"digit": 7},  # state 7
        ]
        curr_state = 0  # initial state
        for ch in s:
            if ch.isdigit():
                group = "digit"
            elif ch in "+-":
                group = "sign"
            elif ch in "eE":
                group = "exponent"
            elif ch == ".":
                group = "dot"
            else:
                # invalid letter
                return False

            # check for invalid transition
            if group not in dfa[curr_state]:
                return False
            curr_state = dfa[curr_state][group]

        # check if curr_state in one of ending states
        return curr_state in [1, 4, 7]
    
import pytest  # noqa: E402

@pytest.fixture(params=[SolutionNatural, SolutionStateMachine], 
                ids=["Natural", "StateMachine"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Input: s = "0" -> Output: True"""
    assert solution_instance.isNumber("0") is True

def test_example2(solution_instance):
    """Input: s = "e" -> Output: False"""
    assert solution_instance.isNumber("e") is False

def test_example3(solution_instance):
    """Input: s = "." -> Output: False"""
    assert solution_instance.isNumber(".") is False

def test_valid_integers(solution_instance):
    """Test valid integer numbers."""
    valid_integers = ["2", "0089", "+3", "-0", "42"]
    for num in valid_integers:
        assert solution_instance.isNumber(num) is True

def test_valid_decimals(solution_instance):
    """Test valid decimal numbers."""
    valid_decimals = ["-0.1", "+3.14", "4.", "-.9", "0.1", ".123"]
    for num in valid_decimals:
        assert solution_instance.isNumber(num) is True

def test_valid_with_exponent(solution_instance):
    """Test valid numbers with exponent."""
    valid_with_exponent = ["2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    for num in valid_with_exponent:
        assert solution_instance.isNumber(num) is True

def test_invalid_characters(solution_instance):
    """Test invalid characters in numbers."""
    invalid_chars = ["abc", "1a", "99e2.5", "?123"]
    for num in invalid_chars:
        assert solution_instance.isNumber(num) is False

def test_invalid_structure(solution_instance):
    """Test invalid number structure."""
    invalid_structure = ["1e", "e3", "--6", "-+3", "95a54e53", ".e1", "+.", "++1"]
    for num in invalid_structure:
        assert solution_instance.isNumber(num) is False

def test_invalid_multiple_dots(solution_instance):
    """Test invalid numbers with multiple dots."""
    invalid_multiple_dots = ["1.2.3", "1..2", ".", ".."]
    for num in invalid_multiple_dots:
        assert solution_instance.isNumber(num) is False

def test_invalid_multiple_exponents(solution_instance):
    """Test invalid numbers with multiple exponents."""
    invalid_multiple_exponents = ["1e2e3", "1ee2", "e2e3"]
    for num in invalid_multiple_exponents:
        assert solution_instance.isNumber(num) is False

def test_invalid_exponent_placement(solution_instance):
    """Test invalid placement of exponent."""
    invalid_exponent_placement = ["e", ".e", "e1", "+e3", "-e2"]
    for num in invalid_exponent_placement:
        assert solution_instance.isNumber(num) is False

def test_valid_edge_cases(solution_instance):
    """Test edge cases that should be valid."""
    valid_edge_cases = ["0", "+0", "-0", "0.0", ".0", "0.", "0e0"]
    for num in valid_edge_cases:
        assert solution_instance.isNumber(num) is True

def test_invalid_edge_cases(solution_instance):
    """Test edge cases that should be invalid."""
    invalid_edge_cases = ["", " ", "+", "-", ".", "e", "+e", "-e", ".e", "+.", "-."]
    for num in invalid_edge_cases:
        assert solution_instance.isNumber(num) is False

def test_exponent_with_decimal_point(solution_instance):
    """Test invalid numbers with decimal point in exponent."""
    invalid_exponent_decimal = ["1e1.1", "1e.1", "1.2e1.1"]
    for num in invalid_exponent_decimal:
        assert solution_instance.isNumber(num) is False

def test_signs_in_wrong_position(solution_instance):
    """Test invalid numbers with signs in wrong positions."""
    invalid_signs = ["1+", "1-", "1.+2", "1.-2", "1e1+1", "1e1-1"]
    for num in invalid_signs:
        assert solution_instance.isNumber(num) is False

def test_complex_valid_examples(solution_instance):
    """Test more complex but valid number examples."""
    complex_valid = ["1e+1", "1e-1", "+1.e+5", "-1.e-5", "+.5e+3", "-.5e-3"]
    for num in complex_valid:
        assert solution_instance.isNumber(num) is True

# To run these tests:
# 1. Make sure pytest is installed: pip install pytest
# 2. Navigate to the directory containing the test file and the solution file.
# 3. Run pytest in the terminal: pytest