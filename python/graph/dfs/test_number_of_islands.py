import pytest
from number_of_islands import SolutionDFS

@pytest.fixture
def solution():
    return SolutionDFS()

def test_example_1(solution):
    # Test the first example from the problem statement
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert solution.numIslands(grid) == 1

def test_example_2(solution):
    # Test the second example from the problem statement
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert solution.numIslands(grid) == 3

def test_empty_grid(solution):
    # Test with no land (all water)
    grid = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"]
    ]
    assert solution.numIslands(grid) == 0

def test_full_grid(solution):
    # Test with all land
    grid = [
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["1", "1", "1"]
    ]
    assert solution.numIslands(grid) == 1

def test_single_cell(solution):
    # Test with a single cell
    grid = [["1"]]
    assert solution.numIslands(grid) == 1
    
    grid = [["0"]]
    assert solution.numIslands(grid) == 0

def test_line_grid(solution):
    # Test with a grid that's just a line
    grid = [["1", "0", "1", "0", "1"]]
    assert solution.numIslands(grid) == 3
    
    grid = [["1"], ["0"], ["1"], ["0"], ["1"]]
    assert solution.numIslands(grid) == 3

def test_diagonal_islands(solution):
    # Diagonally adjacent land should be separate islands
    grid = [
        ["1", "0", "1"],
        ["0", "1", "0"],
        ["1", "0", "1"]
    ]
    assert solution.numIslands(grid) == 5

def test_complex_shapes(solution):
    # Test islands with complex shapes
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "0", "0", "0", "0"],
        ["0", "0", "1", "1", "0"],
        ["0", "0", "1", "0", "1"]
    ]
    assert solution.numIslands(grid) == 3

def test_large_grid(solution):
    # Test with a larger grid
    grid = [["0" for _ in range(100)] for _ in range(100)]
    # Create 10 islands
    for i in range(10):
        row, col = i*10, i*10
        grid[row][col] = "1"
    
    assert solution.numIslands(grid) == 10

def test_zigzag_island(solution):
    # Test with a zigzag shaped island
    grid = [
        ["1", "0", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "1", "0", "0", "0"],
        ["0", "1", "1", "0", "0"],
        ["0", "0", "1", "0", "0"]
    ]
    assert solution.numIslands(grid) == 1

def test_boundary_grid(solution):
    # Test with land cells on the boundary
    grid = [
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1"]
    ]
    assert solution.numIslands(grid) == 1

def test_max_constraints(solution):
    # Test close to max constraints (300x300)
    # Creating a smaller version for reasonable test time
    size = 30
    grid = [["0" for _ in range(size)] for _ in range(size)]
    # Create some islands
    for i in range(5):
        for j in range(5):
            grid[i*6][j*6] = "1"
    
    assert solution.numIslands(grid) == 25

def test_larger_grid(solution):
    # Test with a 50x50 grid with various island patterns
    size = 50
    grid = [["0" for _ in range(size)] for _ in range(size)]
    
    # Create a spiral island
    for i in range(10, 40):
        grid[i][10] = "1"  # Left vertical line
        grid[i][40] = "1"  # Right vertical line
    
    for j in range(10, 41):
        grid[10][j] = "1"  # Top horizontal line
        grid[40][j] = "1"  # Bottom horizontal line
    
    # Create some small islands
    for i in range(5):
        grid[i][i] = "1"
        grid[i][size-i-1] = "1"
    
    assert solution.numIslands(grid) == 1 + 5*2  # 1 large spiral + 10 single-cell islands

def test_grid_with_long_islands(solution):
    # Test with a grid that has long snake-like islands
    width, height = 100, 80
    grid = [["0" for _ in range(width)] for _ in range(height)]
    
    # Create 5 horizontal snake islands
    for i in range(5):
        row = i * 15 + 5
        for col in range(5, 95):
            grid[row][col] = "1"
    
    # Create 3 vertical snake islands
    for i in range(3):
        col = i * 30 + 10
        for row in range(5, 75):
            grid[row][col] = "1"
    
    # These should intersect forming fewer islands
    # Count the number of distinct islands (should be less than 8 due to intersections)
    result = solution.numIslands(grid)
    assert result < 8
    assert result > 0

def test_grid_with_many_small_islands(solution):
    # Test with a grid containing many small islands
    width, height = 150, 150
    grid = [["0" for _ in range(width)] for _ in range(height)]
    
    # Create a pattern of islands
    for i in range(0, height, 10):
        for j in range(0, width, 10):
            # Create a small 2x2 island
            if i+1 < height and j+1 < width:
                grid[i][j] = "1"
                grid[i+1][j] = "1"
                grid[i][j+1] = "1"
                grid[i+1][j+1] = "1"
    
    # Should have (150/10) * (150/10) = 15 * 15 = 225 islands
    assert solution.numIslands(grid) == 225

def test_random_grid(solution):
    # Test with a randomized grid
    import random
    random.seed(42)  # For reproducibility
    
    width, height = 120, 120
    grid = [["0" for _ in range(width)] for _ in range(height)]
    
    # Randomly place land with 20% probability
    for i in range(height):
        for j in range(width):
            if random.random() < 0.2:
                grid[i][j] = "1"
    
    # We don't know exactly how many islands there will be,
    # but we can ensure the function runs without errors
    result = solution.numIslands(grid)
    assert result >= 0

def test_grid_edge_islands(solution):
    # Test with islands that touch the edges of the grid
    width, height = 100, 100
    grid = [["0" for _ in range(width)] for _ in range(height)]
    
    # Create a border of land
    for i in range(height):
        grid[i][0] = "1"  # Left edge
        grid[i][width-1] = "1"  # Right edge
    
    for j in range(width):
        grid[0][j] = "1"  # Top edge
        grid[height-1][j] = "1"  # Bottom edge
    
    # Create some islands inside
    for i in range(10):
        for j in range(10):
            grid[20+i][20+j] = "1"
            grid[60+i][60+j] = "1"
    
    # Should have 1 border island + 2 interior islands
    assert solution.numIslands(grid) == 3

def test_grid_at_constraints_limit(solution):
    # Test with grid at the constraints limit (but reduced for test performance)
    # Actual constraint is 300x300, but we'll use a smaller grid for test performance
    width, height = 200, 200
    grid = [["0" for _ in range(width)] for _ in range(height)]
    
    # Create a checkerboard pattern of single-cell islands
    for i in range(0, height, 2):
        for j in range(0, width, 2):
            grid[i][j] = "1"
    
    # Should have (200/2) * (200/2) = 100 * 100 = 10000 islands
    result = solution.numIslands(grid)
    assert result == 10000