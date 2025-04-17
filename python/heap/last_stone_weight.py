# https://leetcode.com/problems/last-stone-weight/description/
"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1
 

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # multiply with -1, to use heapq of negative values
        # the min heap is now functioning as a max heap with heapq
        arr = [stone * (-1) for stone in stones]
        heapq.heapify(arr)
        while len(arr) >= 2:
            top_pick = heapq.heappop(arr)
            second_pick = heapq.heappop(arr)
            if top_pick == second_pick:
                continue
            else:
                # abs(top_pick) is higher than abs(second_pick)
                remaining_stone = top_pick - second_pick  # this is negative
                heapq.heappush(arr, remaining_stone)

        return abs(arr[0]) if len(arr) == 1 else 0


import pytest  # noqa: E402

@pytest.fixture
def solution():
    """Fixture that provides the solution implementation."""
    return Solution()

def test_example_1(solution):
    """Test the first example from the problem statement."""
    stones = [2, 7, 4, 1, 8, 1]
    assert solution.lastStoneWeight(stones) == 1

def test_example_2(solution):
    """Test the second example from the problem statement."""
    stones = [1]
    assert solution.lastStoneWeight(stones) == 1

def test_empty_stones(solution):
    """Test with an empty array (should not happen given constraints but testing for completeness)."""
    stones = []
    try:
        result = solution.lastStoneWeight(stones)
        assert result == 0  # If handled, should return 0
    except Exception:  # Changed from bare except
        pass  # If not handled, an exception is acceptable

def test_two_equal_stones(solution):
    """Test with two stones of equal weight."""
    stones = [5, 5]
    assert solution.lastStoneWeight(stones) == 0

def test_all_stones_destroyed(solution):
    """Test when all stones are destroyed."""
    stones = [2, 2, 2, 2]  # All stones will be destroyed
    assert solution.lastStoneWeight(stones) == 0

def test_large_stones(solution):
    """Test with stones at the maximum weight."""
    stones = [1000, 1000, 1000]  # After smashing, one 1000 weight stone remains
    assert solution.lastStoneWeight(stones) == 1000

def test_different_weights(solution):
    """Test with stones of different weights."""
    stones = [10, 5, 3, 8]
    # 10 & 8 -> 2, then 5 & 3 -> 2, then 2 & 2 -> 0
    assert solution.lastStoneWeight(stones) == 0

def test_minimum_constraints(solution):
    """Test with the minimum constraints."""
    stones = [1]  # Minimum length is 1
    assert solution.lastStoneWeight(stones) == 1

def test_maximum_constraints(solution):
    """Test with values near the maximum constraints."""
    # Create an array of 30 stones (max length) with max weight
    stones = [1000] * 30
    # All pairs will be destroyed (since they're equal), but since there are 30 stones (even number),
    # there will be no stone left
    assert solution.lastStoneWeight(stones) == 0

def test_odd_number_of_stones(solution):
    """Test with an odd number of stones."""
    stones = [3, 3, 3]
    # 3 & 3 -> 0, leaving one stone of weight 3
    assert solution.lastStoneWeight(stones) == 3

def test_pattern_requiring_multiple_smashes(solution):
    """Test with a pattern that requires multiple rounds of smashing."""
    stones = [2, 7, 4, 1, 8, 1]
    # This is the example case but testing it separately for clarity
    # 8 & 7 -> 1, [2,4,1,1,1], then 4 & 2 -> 2, [2,1,1,1], etc.
    assert solution.lastStoneWeight(stones) == 1

def test_specific_case_with_progression(solution):
    """Test a specific case with a clear progression."""
    stones = [10, 5, 8, 7]
    # 10 & 8 -> 2, [5,7,2], then 7 & 5 -> 2, [2,2], then 2 & 2 -> 0, []
    assert solution.lastStoneWeight(stones) == 0

def test_increasing_sequence(solution):
    """Test with an increasing sequence of weights."""
    stones = [1, 2, 3, 4, 5]
    # 5 & 4 -> 1, arr = [-3, -2, -1, -1]
    # 3 & 2 -> 1, arr = [-1, -1, -1]
    # 1 & 1 -> 0, arr = [-1]
    # 1 & 1 -> 0, arr = [] -> This is wrong, should be [-1]
    # Let's trace again:
    # stones = [1, 2, 3, 4, 5] -> arr = [-5, -4, -3, -2, -1]
    # pop -5, -4 -> push -1 -> arr = [-3, -2, -1, -1]
    # pop -3, -2 -> push -1 -> arr = [-1, -1, -1]
    # pop -1, -1 -> push 0 -> arr = [-1, 0] -> This is wrong, if equal they are destroyed
    # pop -1, -1 -> continue -> arr = [-1]
    # Final result should be abs(-1) = 1
    assert solution.lastStoneWeight(stones) == 1

def test_single_large_stone(solution):
    """Test with a single large stone."""
    stones = [999]
    assert solution.lastStoneWeight(stones) == 999

def test_two_different_stones(solution):
    """Test with just two stones of different weights."""
    stones = [10, 4]
    # 10 & 4 -> 6
    assert solution.lastStoneWeight(stones) == 6

def test_final_stone_not_zero_or_one(solution):
    """Test a case where the final stone has a weight other than 0 or 1."""
    stones = [3, 7, 2]
    # 7 & 3 -> 4, [4, 2]
    # 4 & 2 -> 2, [2]
    assert solution.lastStoneWeight(stones) == 2

def test_mixed_large_small_stones(solution):
    """Test with a mix of very large and very small stones."""
    stones = [1000, 1, 2, 3]
    # 1000 & 3 -> 997, [997, 1, 2]
    # 997 & 2 -> 995, [995, 1]
    # 995 & 1 -> 994, [994]
    assert solution.lastStoneWeight(stones) == 994

def test_duplicate_weights_mixed(solution):
    """Test with duplicate weights mixed with other weights."""
    stones = [5, 8, 5, 8, 3]
    # 8 & 8 -> 0, [5, 5, 3]
    # 5 & 5 -> 0, [3]
    assert solution.lastStoneWeight(stones) == 3

if __name__ == "__main__":
    # Simple manual test
    sol = Solution()
    print(sol.lastStoneWeight([2, 7, 4, 1, 8, 1]))  # Expected: 1

