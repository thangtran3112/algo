import pytest
from next_right_perfect_tree import Solution, Node

def create_perfect_tree(values):
    """Helper function to create a perfect binary tree from a list of values."""
    if not values:
        return None
    
    # Create all nodes first
    nodes = [Node(val) if val is not None else None for val in values]
    
    # Connect nodes
    for i in range(len(nodes)):
        if nodes[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            
            if left_index < len(nodes):
                nodes[i].left = nodes[left_index]
            if right_index < len(nodes):
                nodes[i].right = nodes[right_index]
    
    return nodes[0] if nodes else None

def get_level_order_with_next(root):
    """Convert tree with next pointers to level order traversal with # markers."""
    if not root:
        return []
    
    result = []
    level_start = root
    
    # Traverse each level
    while level_start:
        current = level_start
        result.append(current.val)
        
        # Traverse the current level using next pointers
        while current.next:
            current = current.next
            result.append(current.val)
        
        result.append("#")  # End of level marker
        level_start = level_start.left  # Move to the start of next level
    
    return result

class TestNextRightPerfectTree:
    def test_empty_tree(self):
        solution = Solution()
        result = solution.connect(None)
        assert result is None
    
    def test_single_node_tree(self):
        solution = Solution()
        root = Node(1)
        result = solution.connect(root)
        assert result.val == 1
        assert result.next is None
    
    def test_perfect_tree_three_nodes(self):
        solution = Solution()
        root = create_perfect_tree([1, 2, 3])
        result = solution.connect(root)
        
        assert result.val == 1
        assert result.next is None
        assert result.left.val == 2
        assert result.left.next == result.right
        assert result.right.val == 3
        assert result.right.next is None
    
    def test_perfect_tree_seven_nodes(self):
        solution = Solution()
        root = create_perfect_tree([1, 2, 3, 4, 5, 6, 7])
        result = solution.connect(root)
        
        # Level 0
        assert result.val == 1
        assert result.next is None
        
        # Level 1
        assert result.left.val == 2
        assert result.left.next == result.right
        assert result.right.val == 3
        assert result.right.next is None
        
        # Level 2
        assert result.left.left.val == 4
        assert result.left.left.next == result.left.right
        assert result.left.right.val == 5
        assert result.left.right.next == result.right.left
        assert result.right.left.val == 6
        assert result.right.left.next == result.right.right
        assert result.right.right.val == 7
        assert result.right.right.next is None
    
    def test_perfect_tree_fifteen_nodes(self):
        solution = Solution()
        values = list(range(1, 16))  # 1-15
        root = create_perfect_tree(values)
        result = solution.connect(root)
        
        level_order = get_level_order_with_next(result)
        expected = [1, "#", 2, 3, "#", 4, 5, 6, 7, "#", 8, 9, 10, 11, 12, 13, 14, 15, "#"]
        
        # Test just a few key connections for this larger tree
        assert result.left.left.next == result.left.right
        assert result.left.right.next == result.right.left
        assert result.right.left.next == result.right.right
        assert result.right.right.next is None
        
        # Check all connections via level order traversal
        assert level_order == expected

if __name__ == "__main__":
    pytest.main()