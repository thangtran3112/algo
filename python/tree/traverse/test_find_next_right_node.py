import pytest
from find_next_right_node import Solution, SolutionBFS, TreeNode

@pytest.fixture
def recursive_solution():
    return Solution()

@pytest.fixture
def bfs_solution():
    return SolutionBFS()

@pytest.mark.parametrize("solution_class", [Solution, SolutionBFS])
class TestConnect:
    def test_empty_tree(self, solution_class):
        """Test with an empty tree."""
        solution = solution_class()
        root = None
        result = solution.connect(root)
        assert result is None

    def test_single_node(self, solution_class):
        """Test with a single node tree."""
        solution = solution_class()
        root = TreeNode(1)
        result = solution.connect(root)
        assert result.val == 1
        assert result.next is None

    def test_complete_tree(self, solution_class):
        """Test with a small perfect binary tree."""
        solution = solution_class()
        # Create a tree [1,2,3,4,5,6,7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        result = solution.connect(root)
        
        # Check level 1
        assert result.next is None
        
        # Check level 2
        assert result.left.next == result.right
        assert result.right.next is None
        
        # Check level 3
        assert result.left.left.next == result.left.right
        assert result.left.right.next == result.right.left
        assert result.right.left.next == result.right.right
        assert result.right.right.next is None

    def test_larger_tree(self, solution_class):
        """Test with a larger perfect binary tree."""
        solution = solution_class()
        # Create a 3-level perfect binary tree
        root = TreeNode(1)
        # Level 2
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        # Level 3
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        # Level 4
        root.left.left.left = TreeNode(8)
        root.left.left.right = TreeNode(9)
        root.left.right.left = TreeNode(10)
        root.left.right.right = TreeNode(11)
        root.right.left.left = TreeNode(12)
        root.right.left.right = TreeNode(13)
        root.right.right.left = TreeNode(14)
        root.right.right.right = TreeNode(15)
        
        result = solution.connect(root)
        
        # Check level 1
        assert result.next is None
        
        # Check level 2
        assert result.left.next == result.right
        assert result.right.next is None
        
        # Check level 3
        assert result.left.left.next == result.left.right
        assert result.left.right.next == result.right.left
        assert result.right.left.next == result.right.right
        assert result.right.right.next is None
        
        # Check level 4
        assert result.left.left.left.next == result.left.left.right
        assert result.left.left.right.next == result.left.right.left
        assert result.left.right.left.next == result.left.right.right
        assert result.left.right.right.next == result.right.left.left
        assert result.right.left.left.next == result.right.left.right
        assert result.right.left.right.next == result.right.right.left
        assert result.right.right.left.next == result.right.right.right
        assert result.right.right.right.next is None

    def test_negative_values(self, solution_class):
        """Test with negative values in the tree."""
        solution = solution_class()
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        
        result = solution.connect(root)
        
        assert result.val == -1
        assert result.left.next == result.right
        assert result.right.next is None

    def test_boundary_values(self, solution_class):
        """Test with boundary values from the constraints."""
        solution = solution_class()
        root = TreeNode(1000)
        root.left = TreeNode(-1000)
        root.right = TreeNode(1000)
        
        result = solution.connect(root)
        
        assert result.val == 1000
        assert result.left.next == result.right
        assert result.right.next is None