import pytest
from courses_schedule import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    numCourses = 2
    prerequisites = [[1, 0]]
    result = solution.findOrder(numCourses, prerequisites)
    assert len(result) == numCourses
    assert result[0] == 0
    assert result[1] == 1

def test_example_2(solution):
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result = solution.findOrder(numCourses, prerequisites)
    assert len(result) == numCourses
    
    # Verify topological ordering
    course_positions = {course: i for i, course in enumerate(result)}
    for course, prereq in prerequisites:
        assert course_positions[prereq] < course_positions[course]

def test_example_3(solution):
    numCourses = 1
    prerequisites = []
    result = solution.findOrder(numCourses, prerequisites)
    assert result == [0]

def test_impossible_courses(solution):
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]  # Cycle: 0->1->0
    result = solution.findOrder(numCourses, prerequisites)
    assert result == []

def test_large_courses_no_prerequisites(solution):
    numCourses = 2000
    prerequisites = []
    result = solution.findOrder(numCourses, prerequisites)
    assert len(result) == numCourses
    assert set(result) == set(range(numCourses))

def test_chain_dependency(solution):
    numCourses = 5
    prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3]]
    result = solution.findOrder(numCourses, prerequisites)
    assert result == [0, 1, 2, 3, 4]

def test_complex_dependencies(solution):
    numCourses = 6
    prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [5, 2]]
    result = solution.findOrder(numCourses, prerequisites)
    assert len(result) == numCourses
    
    # Verify topological ordering
    course_positions = {course: i for i, course in enumerate(result)}
    for course, prereq in prerequisites:
        assert course_positions[prereq] < course_positions[course]

def test_multiple_valid_orderings(solution):
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result = solution.findOrder(numCourses, prerequisites)
    assert len(result) == numCourses
    
    # Possible orderings are [0,1,2,3] or [0,2,1,3]
    course_positions = {course: i for i, course in enumerate(result)}
    assert course_positions[0] < course_positions[1]
    assert course_positions[0] < course_positions[2]
    assert course_positions[1] < course_positions[3]
    assert course_positions[2] < course_positions[3]

def test_complex_cycle(solution):
    numCourses = 6
    prerequisites = [[1, 0], [2, 1], [3, 2], [0, 3], [4, 5]]
    result = solution.findOrder(numCourses, prerequisites)
    assert result == []

def test_multiple_components(solution):
    numCourses = 6
    prerequisites = [[1, 0], [3, 2], [5, 4]]
    result = solution.findOrder(numCourses, prerequisites)
    assert len(result) == numCourses
    
    # Check ordering within each component
    course_positions = {course: i for i, course in enumerate(result)}
    assert course_positions[0] < course_positions[1]
    assert course_positions[2] < course_positions[3]
    assert course_positions[4] < course_positions[5]

def test_no_prerequisites(solution):
    numCourses = 5
    prerequisites = []
    result = solution.findOrder(numCourses, prerequisites)
    assert len(result) == numCourses
    assert set(result) == set(range(numCourses))

def test_self_dependency(solution):
    numCourses = 3
    prerequisites = [[0, 0]]  # Self-cycle is not allowed by problem constraints
    result = solution.findOrder(numCourses, prerequisites)
    assert result == []