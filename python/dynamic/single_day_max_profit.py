# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from functools import lru_cache
from typing import List

# Easy solution by recursively memorized the largest element after i position
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0

        # find the largest element from i to the end
        # using cache to remember the result
        # space O(n)
        @lru_cache(maxsize=None)
        def findMax(i):
            # base case
            if i == n - 1:
                return prices[n - 1]
            result = max(prices[i], findMax(i + 1))
            return result
        # Time O(n)
        findMax(0)

        # Time O(n)
        for i in range(n - 1):
            max_from_i = findMax(i)
            if prices[i] < max_from_i:
                max_profit = max(max_profit, max_from_i - prices[i])

        return max_profit
        
# Time O(n), Space O(1)
class SolutionNoExtraSpace:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit
    
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture(params=[Solution, SolutionNoExtraSpace],
               ids=["Memoization", "Constant Space"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    prices = [7, 1, 5, 3, 6, 4]
    expected = 5
    assert solution_instance.maxProfit(prices) == expected

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    prices = [7, 6, 4, 3, 1]
    expected = 0
    assert solution_instance.maxProfit(prices) == expected

def test_single_price(solution_instance):
    """Test with a single price."""
    prices = [5]
    expected = 0  # Can't make any profit with just one price
    assert solution_instance.maxProfit(prices) == expected

def test_two_prices_ascending(solution_instance):
    """Test with two prices in ascending order."""
    prices = [1, 2]
    expected = 1
    assert solution_instance.maxProfit(prices) == expected

def test_two_prices_descending(solution_instance):
    """Test with two prices in descending order."""
    prices = [2, 1]
    expected = 0
    assert solution_instance.maxProfit(prices) == expected

def test_same_prices(solution_instance):
    """Test with all same prices."""
    prices = [5, 5, 5, 5]
    expected = 0
    assert solution_instance.maxProfit(prices) == expected

def test_ascending_prices(solution_instance):
    """Test with strictly ascending prices."""
    prices = [1, 2, 3, 4, 5]
    expected = 4
    assert solution_instance.maxProfit(prices) == expected

def test_descending_prices(solution_instance):
    """Test with strictly descending prices."""
    prices = [5, 4, 3, 2, 1]
    expected = 0
    assert solution_instance.maxProfit(prices) == expected

def test_v_shaped_prices(solution_instance):
    """Test with V-shaped prices."""
    prices = [5, 4, 3, 2, 1, 2, 3, 4, 5]
    expected = 4
    assert solution_instance.maxProfit(prices) == expected

def test_mountain_shaped_prices(solution_instance):
    """Test with mountain-shaped prices."""
    prices = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    expected = 4
    assert solution_instance.maxProfit(prices) == expected

def test_valley_peak_valley(solution_instance):
    """Test with valley-peak-valley pattern."""
    prices = [3, 1, 4, 1, 5]
    expected = 4
    assert solution_instance.maxProfit(prices) == expected

def test_large_price_difference(solution_instance):
    """Test with large price difference."""
    prices = [1, 10000]
    expected = 9999
    assert solution_instance.maxProfit(prices) == expected

def test_maximum_prices(solution_instance):
    """Test with prices at the maximum constraint."""
    prices = [10000] * 5
    expected = 0
    assert solution_instance.maxProfit(prices) == expected

def test_max_profit_at_beginning(solution_instance):
    """Test when the max profit is at the beginning of the array."""
    prices = [1, 10, 2, 3, 4, 5]
    expected = 9
    assert solution_instance.maxProfit(prices) == expected

def test_max_profit_at_end(solution_instance):
    """Test when the max profit is at the end of the array."""
    prices = [5, 4, 3, 2, 1, 10]
    expected = 9
    assert solution_instance.maxProfit(prices) == expected

def test_alternating_prices(solution_instance):
    """Test with alternating high-low prices."""
    prices = [1, 10, 1, 10, 1, 10]
    expected = 9
    assert solution_instance.maxProfit(prices) == expected