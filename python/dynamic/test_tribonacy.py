import pytest
from tribonacy import BottomUpSolution, TopDownSolution

# pytest -v test_tribonacy.py


@pytest.fixture
def solutions():
    return BottomUpSolution(), TopDownSolution()


def test_tribonacci_base_cases(solutions):
    bottomUpSolution, topDownSolution = solutions

    # Test base cases
    assert bottomUpSolution.tribonacci(0) == 0
    assert bottomUpSolution.tribonacci(1) == 1
    assert bottomUpSolution.tribonacci(2) == 1

    # Test base cases
    assert topDownSolution.tribonacci(0) == 0
    assert topDownSolution.tribonacci(1) == 1
    assert topDownSolution.tribonacci(2) == 1


def test_tribonacci_small_values(solutions):
    bottomUpSolution, topDownSolution = solutions

    assert bottomUpSolution.tribonacci(3) == 2
    assert bottomUpSolution.tribonacci(4) == 4
    assert bottomUpSolution.tribonacci(5) == 7
    assert bottomUpSolution.tribonacci(6) == 13

    assert topDownSolution.tribonacci(3) == 2
    assert topDownSolution.tribonacci(4) == 4
    assert topDownSolution.tribonacci(5) == 7
    assert topDownSolution.tribonacci(6) == 13


def test_tribonacci_sequence_pattern(solutions):
    bottomUpSolution, topDownSolution = solutions

    """Test that several consecutive values follow the Tribonacci pattern"""
    values = [bottomUpSolution.tribonacci(i) for i in range(10)]
    # Check that T(n) = T(n-1) + T(n-2) + T(n-3) for n >= 3
    for i in range(3, len(values)):
        assert values[i] == values[i - 1] + values[i - 2] + values[i - 3]

    values = [topDownSolution.tribonacci(i) for i in range(10)]
    # Check that T(n) = T(n-1) + T(n-2) + T(n-3) for n >= 3
    for i in range(3, len(values)):
        assert values[i] == values[i - 1] + values[i - 2] + values[i - 3]


def test_tribonacci_example_from_problem(solutions):
    """Test the examples given in the problem statement"""
    bottomUpSolution, topDownSolution = solutions
    assert bottomUpSolution.tribonacci(25) == 1389537
    assert topDownSolution.tribonacci(25) == 1389537


def test_tribonacci_edge_cases(solutions):
    """Test the edge cases from the constraints"""
    bottomUpSolution, topDownSolution = solutions

    assert bottomUpSolution.tribonacci(37) == 2082876103
    assert topDownSolution.tribonacci(37) == 2082876103
    # 2082876103 is less than 2^31 - 1, so it fits in a 32-bit integer


def test_tribonacci_consecutive_values(solutions):
    """Test a sequence of consecutive values to ensure correctness"""
    bottomUpSolution, topDownSolution = solutions
    expected = [0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149]

    for i, expected_val in enumerate(expected):
        assert bottomUpSolution.tribonacci(i) == expected_val

    for i, expected_val in enumerate(expected):
        assert topDownSolution.tribonacci(i) == expected_val
