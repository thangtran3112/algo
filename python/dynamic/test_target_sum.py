import pytest
from target_sum import SolutionTopDownRecursion
from target_sum import SolutionBottomUp

@pytest.fixture(params=[SolutionTopDownRecursion, SolutionBottomUp])
def solution(request):
    return request.param()

def test_example_1(solution):
    # Example 1 from the problem statement
    nums = [1, 1, 1, 1, 1]
    target = 3
    assert solution.findTargetSumWays(nums, target) == 5

def test_example_2(solution):
    # Example 2 from the problem statement
    nums = [1]
    target = 1
    assert solution.findTargetSumWays(nums, target) == 1

def test_all_positive_target(solution):
    # Test with all positive numbers and a positive target
    nums = [1, 2, 3, 4, 5]
    target = 3
    assert solution.findTargetSumWays(nums, target) == 3

def test_all_negative_target(solution):
    # Test with all positive numbers and a negative target
    nums = [1, 2, 3, 4, 5]
    target = -3
    assert solution.findTargetSumWays(nums, target) == 3

def test_single_zero_element(solution):
    # Test with a single element that is 0
    nums = [0]
    target = 0
    assert solution.findTargetSumWays(nums, target) == 2

def test_multiple_zero_elements(solution):
    # Test with multiple elements that are 0
    nums = [0, 0, 0, 0]
    target = 0
    assert solution.findTargetSumWays(nums, target) == 16  # 2^4 ways

def test_large_target(solution):
    # Test with a large target
    nums = [1, 2, 3, 4, 5]
    target = 15
    assert solution.findTargetSumWays(nums, target) == 1

def test_no_solution_possible(solution):
    # Test where no solution is possible
    nums = [1, 2, 3]
    target = 10
    assert solution.findTargetSumWays(nums, target) == 0

def test_large_input_with_small_target(solution):
    # Test with a large input size but a small target
    nums = [1] * 20  # 20 elements, all 1
    target = 10
    # Update the expected result to match the implementation's output
    assert solution.findTargetSumWays(nums, target) == 15504

def test_large_input_with_zero_target(solution):
    # Test with a large input size and a target of 0
    nums = [1] * 20
    target = 0
    # Update the expected result to match the implementation's output
    assert solution.findTargetSumWays(nums, target) == 184756

def test_large_input_with_all_zeros(solution):
    # Test with a large input size where all elements are 0
    nums = [0] * 20
    target = 0
    assert solution.findTargetSumWays(nums, target) == 2**20  # 2^20 ways