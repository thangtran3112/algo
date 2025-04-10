import pytest
from find_duplicate import SolutionBST, SolutionFastSlow

@pytest.fixture
def bst_solution():
    return SolutionBST()

@pytest.fixture
def fastslow_solution():
    return SolutionFastSlow()

def test_example_1_bst(bst_solution):
    """Test the first example from the problem statement with BST solution."""
    nums = [1, 3, 4, 2, 2]
    assert bst_solution.findDuplicate(nums) == 2

def test_example_1_fastslow(fastslow_solution):
    """Test the first example from the problem statement with Floyd's algorithm."""
    nums = [1, 3, 4, 2, 2]
    assert fastslow_solution.findDuplicate(nums) == 2

def test_example_2_bst(bst_solution):
    """Test the second example from the problem statement with BST solution."""
    nums = [3, 1, 3, 4, 2]
    assert bst_solution.findDuplicate(nums) == 3

def test_example_2_fastslow(fastslow_solution):
    """Test the second example from the problem statement with Floyd's algorithm."""
    nums = [3, 1, 3, 4, 2]
    assert fastslow_solution.findDuplicate(nums) == 3

def test_example_3_bst(bst_solution):
    """Test the third example from the problem statement with BST solution."""
    nums = [3, 3, 3, 3, 3]
    assert bst_solution.findDuplicate(nums) == 3

def test_example_3_fastslow(fastslow_solution):
    """Test the third example from the problem statement with Floyd's algorithm."""
    nums = [3, 3, 3, 3, 3]
    assert fastslow_solution.findDuplicate(nums) == 3

def test_minimal_array_bst(bst_solution):
    """Test with the smallest possible array with BST solution."""
    nums = [1, 1]
    assert bst_solution.findDuplicate(nums) == 1

def test_minimal_array_fastslow(fastslow_solution):
    """Test with the smallest possible array with Floyd's algorithm."""
    nums = [1, 1]
    assert fastslow_solution.findDuplicate(nums) == 1

def test_duplicate_at_beginning_bst(bst_solution):
    """Test with duplicate at the beginning with BST solution."""
    nums = [1, 1, 2, 3, 4]
    assert bst_solution.findDuplicate(nums) == 1

def test_duplicate_at_beginning_fastslow(fastslow_solution):
    """Test with duplicate at the beginning with Floyd's algorithm."""
    nums = [1, 1, 2, 3, 4]
    assert fastslow_solution.findDuplicate(nums) == 1

def test_duplicate_at_end_bst(bst_solution):
    """Test with duplicate at the end with BST solution."""
    nums = [1, 2, 3, 4, 4]
    assert bst_solution.findDuplicate(nums) == 4

def test_duplicate_at_end_fastslow(fastslow_solution):
    """Test with duplicate at the end with Floyd's algorithm."""
    nums = [1, 2, 3, 4, 4]
    assert fastslow_solution.findDuplicate(nums) == 4

def test_multiple_duplicates_bst(bst_solution):
    """Test with multiple instances of the duplicate with BST solution."""
    nums = [2, 2, 2, 2, 2]
    assert bst_solution.findDuplicate(nums) == 2

def test_multiple_duplicates_fastslow(fastslow_solution):
    """Test with multiple instances of the duplicate with Floyd's algorithm."""
    nums = [2, 2, 2, 2, 2]
    assert fastslow_solution.findDuplicate(nums) == 2

def test_large_array_bst(bst_solution):
    """Test with a larger array to verify efficiency with BST solution."""
    # Create an array [1,2,3,...,999,1000,1000]
    nums = list(range(1, 1001)) + [1000]
    assert bst_solution.findDuplicate(nums) == 1000

def test_large_array_fastslow(fastslow_solution):
    """Test with a larger array to verify efficiency with Floyd's algorithm."""
    # Create an array [1,2,3,...,999,1000,1000]
    nums = list(range(1, 1001)) + [1000]
    assert fastslow_solution.findDuplicate(nums) == 1000

def test_randomly_placed_duplicate_bst(bst_solution):
    """Test with randomly placed duplicate with BST solution."""
    nums = [5, 2, 1, 3, 5, 4]
    assert bst_solution.findDuplicate(nums) == 5

def test_randomly_placed_duplicate_fastslow(fastslow_solution):
    """Test with randomly placed duplicate with Floyd's algorithm."""
    nums = [5, 2, 1, 3, 5, 4]
    assert fastslow_solution.findDuplicate(nums) == 5