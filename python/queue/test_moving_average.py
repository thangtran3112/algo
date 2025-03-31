import pytest
from moving_average import MovingAverage

def test_example():
    # Test the example from the problem description
    movingAverage = MovingAverage(3)
    assert movingAverage.next(1) == 1.0
    assert movingAverage.next(10) == 5.5
    assert round(movingAverage.next(3), 5) == 4.66667
    assert movingAverage.next(5) == 6.0

def test_window_size_1():
    # Test with window size 1
    movingAverage = MovingAverage(1)
    assert movingAverage.next(1) == 1.0
    assert movingAverage.next(10) == 10.0
    assert movingAverage.next(3) == 3.0
    assert movingAverage.next(5) == 5.0

def test_large_window():
    # Test with larger window size
    movingAverage = MovingAverage(5)
    assert movingAverage.next(1) == 1.0
    assert movingAverage.next(2) == 1.5
    assert movingAverage.next(3) == 2.0
    assert movingAverage.next(4) == 2.5
    assert movingAverage.next(5) == 3.0
    assert movingAverage.next(6) == 4.0  # (2+3+4+5+6)/5

def test_negative_values():
    # Test with negative values
    movingAverage = MovingAverage(3)
    assert movingAverage.next(-1) == -1.0
    assert movingAverage.next(-10) == -5.5
    assert round(movingAverage.next(-3), 5) == -4.66667

def test_mixed_values():
    # Test with mix of positive and negative values
    movingAverage = MovingAverage(3)
    assert movingAverage.next(-5) == -5.0
    assert movingAverage.next(10) == 2.5
    assert round(movingAverage.next(-15), 5) == -3.33333

def test_max_constraints():
    # Test with maximum constraints
    movingAverage = MovingAverage(1000)
    # Fill the window
    sum_val = 0
    for i in range(1, 1001):
        sum_val += i
        assert movingAverage.next(i) == sum_val / i
    
    # Now window is full, test sliding
    for i in range(1001, 1010):
        sum_val = sum_val - (i - 1000) + i
        assert movingAverage.next(i) == sum_val / 1000

def test_extreme_values():
    # Test with extreme values within constraints
    movingAverage = MovingAverage(3)
    assert movingAverage.next(100000) == 100000.0
    assert movingAverage.next(-100000) == 0.0
    # Use pytest's approx or round to handle floating point precision
    assert round(movingAverage.next(100000), 5) == 33333.33333

def test_repeated_values():
    # Test with repeated values
    movingAverage = MovingAverage(4)
    assert movingAverage.next(5) == 5.0
    assert movingAverage.next(5) == 5.0
    assert movingAverage.next(5) == 5.0
    assert movingAverage.next(5) == 5.0
    assert movingAverage.next(5) == 5.0  # Window full of 5s

def test_many_calls():
    # Test with many calls (within constraint of 10^4)
    movingAverage = MovingAverage(2)
    expected = 0
    for i in range(100):  # Just testing 100 calls for brevity
        result = movingAverage.next(i)
        if i == 0:
            expected = 0.0
        elif i == 1:
            expected = 0.5
        else:
            expected = (i-1 + i) / 2
        assert result == expected