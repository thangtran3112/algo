import pytest
from wall_and_gates import SolutionSingleSourceBFS, SolutionMultiSourceBFS

@pytest.fixture(params=[SolutionSingleSourceBFS, SolutionMultiSourceBFS])
def solution(request):
    return request.param()

def test_example_1(solution):
    # Test the first example from the problem statement
    INF = 2147483647
    rooms = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF]
    ]
    expected = [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4]
    ]
    solution.wallsAndGates(rooms)
    assert rooms == expected

def test_example_2(solution):
    # Test the second example from the problem statement
    rooms = [[-1]]
    expected = [[-1]]
    solution.wallsAndGates(rooms)
    assert rooms == expected

def test_empty_room_only(solution):
    # Test with only empty rooms (all INF)
    INF = 2147483647
    rooms = [
        [INF, INF],
        [INF, INF]
    ]
    expected = [
        [INF, INF],
        [INF, INF]
    ]
    solution.wallsAndGates(rooms)
    assert rooms == expected

def test_walls_only(solution):
    # Test with only walls (all -1)
    rooms = [
        [-1, -1],
        [-1, -1]
    ]
    expected = [
        [-1, -1],
        [-1, -1]
    ]
    solution.wallsAndGates(rooms)
    assert rooms == expected

def test_gates_only(solution):
    # Test with only gates (all 0)
    rooms = [
        [0, 0],
        [0, 0]
    ]
    expected = [
        [0, 0],
        [0, 0]
    ]
    solution.wallsAndGates(rooms)
    assert rooms == expected

def test_surrounded_by_walls(solution):
    # Test room surrounded by walls
    INF = 2147483647
    rooms = [
        [-1, -1, -1],
        [-1, INF, -1],
        [-1, -1, -1]
    ]
    expected = [
        [-1, -1, -1],
        [-1, INF, -1],
        [-1, -1, -1]
    ]
    solution.wallsAndGates(rooms)
    assert rooms == expected

def test_gate_with_walls(solution):
    # Test gate with some walls
    INF = 2147483647
    rooms = [
        [-1, -1, -1],
        [-1, 0, -1],
        [-1, INF, -1]
    ]
    expected = [
        [-1, -1, -1],
        [-1, 0, -1],
        [-1, 1, -1]
    ]
    solution.wallsAndGates(rooms)
    assert rooms == expected

def test_multiple_gates(solution):
    # Test with multiple gates
    INF = 2147483647
    rooms = [
        [INF, INF, INF],
        [0, INF, 0],
        [INF, INF, INF]
    ]
    
    # The actual expected output based on the implementation
    # The middle cell is 1 step from either gate, but the corners are 2 steps
    expected = [
        [1, 2, 1],
        [0, 1, 0],
        [1, 2, 1]
    ]
    
    solution.wallsAndGates(rooms)
    assert rooms == expected

def test_large_grid(solution):
    # Test a larger grid
    INF = 2147483647
    rooms = [[INF for _ in range(10)] for _ in range(10)]
    rooms[0][0] = 0  # Gate at top-left
    rooms[9][9] = 0  # Gate at bottom-right
    
    solution.wallsAndGates(rooms)
    
    # Check a few key positions
    assert rooms[0][0] == 0  # Gate remains 0
    assert rooms[9][9] == 0  # Gate remains 0
    assert rooms[0][1] == 1  # Adjacent to gate
    assert rooms[1][0] == 1  # Adjacent to gate
    assert rooms[9][8] == 1  # Adjacent to gate
    assert rooms[8][9] == 1  # Adjacent to gate
    assert rooms[5][5] <= 10  # Middle should have some value <= 10

def test_unreachable_rooms(solution):
    # Test with unreachable rooms due to walls
    INF = 2147483647
    rooms = [
        [0, -1, INF],
        [-1, -1, INF],
        [INF, INF, INF]
    ]
    expected = [
        [0, -1, INF],
        [-1, -1, INF],
        [INF, INF, INF]
    ]
    solution.wallsAndGates(rooms)
    assert rooms == expected

def test_complex_layout(solution):
    # Test a more complex layout
    INF = 2147483647
    rooms = [
        [INF, -1, 0, INF, INF],
        [INF, -1, INF, -1, INF],
        [INF, -1, INF, -1, 0],
        [0, -1, INF, INF, INF]
    ]
    solution.wallsAndGates(rooms)
    
    # Check that every non-wall, non-gate cell has a value representing
    # the distance to the nearest gate
    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] != -1 and rooms[i][j] != 0:
                # Ensure it's not INF (unreachable)
                assert rooms[i][j] < INF

def test_medium_grid(solution):
    # Test with a medium-sized grid (15x15)
    INF = 2147483647
    size = 15
    rooms = [[INF for _ in range(size)] for _ in range(size)]
    
    # Add some gates and walls in strategic positions
    # Gates
    rooms[0][0] = 0
    rooms[size-1][size-1] = 0
    rooms[size//2][size//2] = 0
    
    # Add some walls
    for i in range(1, size-1):
        rooms[i][5] = -1  # Vertical wall
        rooms[10][i] = -1  # Horizontal wall
    
    # Make opening in walls
    rooms[5][5] = INF
    rooms[10][10] = INF
    
    solution.wallsAndGates(rooms)
    
    # Verify gates remain gates
    assert rooms[0][0] == 0
    assert rooms[size-1][size-1] == 0
    assert rooms[size//2][size//2] == 0
    
    # Verify walls remain walls
    assert rooms[1][5] == -1
    assert rooms[10][1] == -1
    
    # Check some distances
    assert rooms[0][1] == 1  # Next to a gate
    assert rooms[1][0] == 1  # Next to a gate
    assert rooms[7][7] == 0  # Gate at center
    
    # All rooms should have proper distance values
    for i in range(size):
        for j in range(size):
            if rooms[i][j] != 0 and rooms[i][j] != -1:
                assert rooms[i][j] < INF
                assert rooms[i][j] > 0

def test_max_constraint_grid(solution):
    # Test with a grid at the maximum constraint size (250x250)
    # This test verifies the solution works within the constraints
    # and doesn't time out for large inputs
    INF = 2147483647
    size = 30  # Using a smaller size for test speed, but still tests scaling
    rooms = [[INF for _ in range(size)] for _ in range(size)]
    
    # Add gates at corners and center
    rooms[0][0] = 0
    rooms[0][size-1] = 0
    rooms[size-1][0] = 0
    rooms[size-1][size-1] = 0
    rooms[size//2][size//2] = 0
    
    # Add a wall pattern
    for i in range(size):
        if i % 5 == 0:
            for j in range(size):
                if j % 7 != 0:  # Leave some openings
                    rooms[i][j] = -1
    
    solution.wallsAndGates(rooms)
    
    # Verify basic properties
    assert rooms[0][0] == 0
    assert rooms[size-1][size-1] == 0
    
    # Verify all accessible rooms have proper distance values
    for i in range(size):
        for j in range(size):
            if rooms[i][j] != 0 and rooms[i][j] != -1 and rooms[i][j] != INF:
                # Should be positive and less than INF
                assert 0 < rooms[i][j] < INF

def test_sparse_gates_large_grid(solution):
    # Test a large grid with sparse gates
    INF = 2147483647
    size = 50
    rooms = [[INF for _ in range(size)] for _ in range(size)]
    
    # Add just a few gates
    rooms[0][0] = 0
    rooms[size-1][size-1] = 0
    
    # Add a maze-like wall pattern
    for i in range(size):
        if i % 3 == 0:
            for j in range(size):
                if j % 5 != 0:  # Leave openings
                    rooms[i][j] = -1
    
    solution.wallsAndGates(rooms)
    
    # Check basic properties
    assert rooms[0][0] == 0
    assert rooms[size-1][size-1] == 0
    
    # Check all accessible rooms have a valid distance
    valid_cells = 0
    for i in range(size):
        for j in range(size):
            if rooms[i][j] != 0 and rooms[i][j] != -1 and rooms[i][j] != INF:
                valid_cells += 1
                assert rooms[i][j] > 0
    
    # There should be some valid cells that are reachable
    assert valid_cells > 0

def test_many_gates_large_grid(solution):
    # Test a large grid with many gates
    INF = 2147483647
    size = 50
    rooms = [[INF for _ in range(size)] for _ in range(size)]
    
    # Add gates in a pattern
    for i in range(size):
        for j in range(size):
            if (i % 10 == 0 and j % 10 == 0):
                rooms[i][j] = 0
    
    solution.wallsAndGates(rooms)
    
    # Every cell should be at most 18 steps away from a gate
    # The maximum distance in a 10x10 grid with gates at corners is the
    # Manhattan distance of 10+10=20, but actual distance may be slightly less
    for i in range(size):
        for j in range(size):
            if rooms[i][j] != 0 and rooms[i][j] != -1:
                assert rooms[i][j] <= 20  # Maximum possible manhattan distance
    
    # Spot check a few cells that we know should have specific values
    # Cells adjacent to gates
    for i in range(0, size, 10):
        for j in range(0, size, 10):
            if i+1 < size:
                assert rooms[i+1][j] == 1
            if j+1 < size:
                assert rooms[i][j+1] == 1