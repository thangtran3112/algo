import pytest
from clone_graph import Solution, Node

class TestCloneGraph:
    def test_empty_graph(self):
        """Test cloning an empty graph (None node)"""
        solution = Solution()
        result = solution.cloneGraph(None)
        assert result is None

    def test_single_node(self):
        """Test cloning a graph with a single node and no neighbors"""
        solution = Solution()
        node = Node(1)
        result = solution.cloneGraph(node)
        
        # Check that the result is not the same object but has same value
        assert result is not node
        assert result.val == 1
        assert len(result.neighbors) == 0

    def test_two_connected_nodes(self):
        """Test cloning a graph with two nodes connected to each other"""
        solution = Solution()
        
        # Create a simple graph: 1 -- 2
        node1 = Node(1)
        node2 = Node(2)
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)
        
        # Clone the graph
        result = solution.cloneGraph(node1)
        
        # Check values and references
        assert result is not node1
        assert result.val == 1
        assert len(result.neighbors) == 1
        
        cloned_node2 = result.neighbors[0]
        assert cloned_node2 is not node2
        assert cloned_node2.val == 2
        assert len(cloned_node2.neighbors) == 1
        assert cloned_node2.neighbors[0] is result  # Circular reference preserved

    def test_complex_graph(self):
        """Test a more complex graph structure"""
        solution = Solution()
        
        # Create a graph with more complex connections
        nodes = [Node(i) for i in range(1, 6)]  # 5 nodes with values 1-5
        
        # Node 1 connects to 2, 3, 4
        nodes[0].neighbors = [nodes[1], nodes[2], nodes[3]]
        
        # Node 2 connects to 1, 5
        nodes[1].neighbors = [nodes[0], nodes[4]]
        
        # Node 3 connects to 1, 4
        nodes[2].neighbors = [nodes[0], nodes[3]]
        
        # Node 4 connects to 1, 3, 5
        nodes[3].neighbors = [nodes[0], nodes[2], nodes[4]]
        
        # Node 5 connects to 2, 4
        nodes[4].neighbors = [nodes[1], nodes[3]]
        
        # Clone the graph starting from node 1
        result = solution.cloneGraph(nodes[0])
        
        # Build a map of cloned nodes for easy access
        visited = set()
        cloned_nodes = {}
        
        def collect_nodes(node):
            if node in visited:
                return
            visited.add(node)
            cloned_nodes[node.val] = node
            for neighbor in node.neighbors:
                collect_nodes(neighbor)
        
        collect_nodes(result)
        
        # Check all 5 nodes are present
        assert len(cloned_nodes) == 5
        
        # Check connections
        assert sorted([n.val for n in cloned_nodes[1].neighbors]) == [2, 3, 4]
        assert sorted([n.val for n in cloned_nodes[2].neighbors]) == [1, 5]
        assert sorted([n.val for n in cloned_nodes[3].neighbors]) == [1, 4]
        assert sorted([n.val for n in cloned_nodes[4].neighbors]) == [1, 3, 5]
        assert sorted([n.val for n in cloned_nodes[5].neighbors]) == [2, 4]

    def test_cyclic_graph(self):
        """Test a graph with cycles (triangle)"""
        solution = Solution()
        
        # Create a triangle graph: 1 -- 2
        #                          | \  |
        #                          |  \ |
        #                          3 -- 4
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        
        node1.neighbors = [node2, node3, node4]
        node2.neighbors = [node1, node4]
        node3.neighbors = [node1, node4]
        node4.neighbors = [node1, node2, node3]
        
        # Clone the graph
        result = solution.cloneGraph(node1)
        
        # Check structure and references
        assert result.val == 1
        assert len(result.neighbors) == 3
        
        # Collect all cloned nodes
        cloned_map = {}
        def collect_nodes(node, original_map=None):
            if original_map is None:
                original_map = {}
            if node.val in original_map:
                return original_map
            original_map[node.val] = node
            for neighbor in node.neighbors:
                collect_nodes(neighbor, original_map)
            return original_map
            
        cloned_map = collect_nodes(result)
        
        # Verify the connections
        assert len(cloned_map) == 4
        assert sorted([n.val for n in cloned_map[1].neighbors]) == [2, 3, 4]
        assert sorted([n.val for n in cloned_map[2].neighbors]) == [1, 4]
        assert sorted([n.val for n in cloned_map[3].neighbors]) == [1, 4]
        assert sorted([n.val for n in cloned_map[4].neighbors]) == [1, 2, 3]

    def test_clone_deep_copy(self):
        """Test that the clone is truly a deep copy with no shared objects"""
        solution = Solution()
        
        # Create a simple graph
        node1 = Node(1)
        node2 = Node(2)
        node1.neighbors = [node2]
        node2.neighbors = [node1]
        
        # Clone the graph
        result = solution.cloneGraph(node1)
        
        # Modify the original graph
        node3 = Node(3)
        node1.neighbors.append(node3)
        node3.neighbors = [node1]
        
        # Check that the clone wasn't affected
        assert len(result.neighbors) == 1
        assert result.neighbors[0].val == 2