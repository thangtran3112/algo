import pytest
from next_greater_letters import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    letters = ["c", "f", "j"]
    target = "a"
    assert solution.nextGreatestLetter(letters, target) == "c"

def test_example_2(solution):
    """Test the second example from the problem statement."""
    letters = ["c", "f", "j"]
    target = "c"
    assert solution.nextGreatestLetter(letters, target) == "f"

def test_example_3(solution):
    """Test the third example from the problem statement."""
    letters = ["x", "x", "y", "y"]
    target = "z"
    assert solution.nextGreatestLetter(letters, target) == "x"

def test_target_greater_than_all_letters(solution):
    """Test when target is greater than all letters."""
    letters = ["a", "b", "c"]
    target = "z"
    assert solution.nextGreatestLetter(letters, target) == "a"

def test_target_less_than_all_letters(solution):
    """Test when target is less than all letters."""
    letters = ["c", "f", "j"]
    target = "a"
    assert solution.nextGreatestLetter(letters, target) == "c"

def test_target_between_letters(solution):
    """Test when target is between letters."""
    letters = ["c", "f", "j"]
    target = "d"
    assert solution.nextGreatestLetter(letters, target) == "f"

def test_duplicate_letters(solution):
    """Test with duplicate letters in the array."""
    letters = ["a", "a", "b", "b", "c", "c"]
    target = "a"
    assert solution.nextGreatestLetter(letters, target) == "b"

def test_all_same_letter(solution):
    """Test when all letters are the same."""
    letters = ["a", "a", "a", "a"]
    target = "a"
    # Since all letters are 'a' and not greater than target 'a', we wrap around
    assert solution.nextGreatestLetter(letters, target) == "a"

def test_minimum_array_size(solution):
    """Test with minimum array size of 2."""
    letters = ["a", "z"]
    target = "a"
    assert solution.nextGreatestLetter(letters, target) == "z"
    
    letters = ["a", "z"]
    target = "z"
    assert solution.nextGreatestLetter(letters, target) == "a"

def test_target_is_last_letter(solution):
    """Test when target is the last letter in the sorted array."""
    letters = ["a", "b", "c", "d", "e"]
    target = "e"
    assert solution.nextGreatestLetter(letters, target) == "a"

def test_adjacent_letters(solution):
    """Test with adjacent letters in the alphabet."""
    letters = ["a", "b", "c", "d", "e"]
    target = "b"
    assert solution.nextGreatestLetter(letters, target) == "c"

def test_non_adjacent_letters(solution):
    """Test with non-adjacent letters in the alphabet."""
    letters = ["a", "e", "i", "o", "u"]
    target = "e"
    assert solution.nextGreatestLetter(letters, target) == "i"

def test_large_array(solution):
    """Test with a larger array to verify binary search efficiency."""
    letters = [chr(ord('a') + i % 26) for i in range(10000)]  # Generate a large array
    target = "m"
    assert solution.nextGreatestLetter(letters, target) == "n"

def test_edge_case_wrap_around(solution):
    """Test the wrap-around case with edge characters."""
    letters = ["a", "b", "c"]
    target = "c"
    assert solution.nextGreatestLetter(letters, target) == "a"