import pytest
from cheap_flight_k_stops import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example_1(solution):
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 1
    assert solution.findCheapestPrice(n, flights, src, dst, k) == 700

def test_example_2(solution):
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    assert solution.findCheapestPrice(n, flights, src, dst, k) == 200

def test_example_3(solution):
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    assert solution.findCheapestPrice(n, flights, src, dst, k) == 500

def test_no_flights(solution):
    n = 3
    flights = []
    src = 0
    dst = 2
    k = 1
    assert solution.findCheapestPrice(n, flights, src, dst, k) == -1

def test_unreachable_destination(solution):
    n = 4
    flights = [[0, 1, 100], [1, 2, 100]]
    src = 0
    dst = 3
    k = 1
    assert solution.findCheapestPrice(n, flights, src, dst, k) == -1

def test_large_k(solution):
    n = 5
    flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [3, 4, 100]]
    src = 0
    dst = 4
    k = 3
    assert solution.findCheapestPrice(n, flights, src, dst, k) == 400

def test_zero_cost_flight(solution):
    n = 3
    flights = [[0, 1, 0], [1, 2, 0]]
    src = 0
    dst = 2
    k = 1
    assert solution.findCheapestPrice(n, flights, src, dst, k) == 0

def test_negative_cost_flight(solution):
    n = 3
    flights = [[0, 1, -100], [1, 2, 100]]
    src = 0
    dst = 2
    k = 1
    assert solution.findCheapestPrice(n, flights, src, dst, k) == 0  # Bellman-Ford handles negative weights

def test_large_graph(solution):
    n = 100
    flights = [[i, i + 1, 100] for i in range(99)]
    src = 0
    dst = 99
    k = 99
    assert solution.findCheapestPrice(n, flights, src, dst, k) == 9900

def test_multiple_paths(solution):
    n = 4
    flights = [[0, 1, 100], [0, 2, 500], [1, 2, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 2
    assert solution.findCheapestPrice(n, flights, src, dst, k) == 400

def test_no_stops_allowed(solution):
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100]]
    src = 0
    dst = 3
    k = 0
    assert solution.findCheapestPrice(n, flights, src, dst, k) == -1