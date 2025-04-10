# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # splitting point within [left, mid]
            if nums[left] > nums[mid]:
                # [4,0,1,2,3]
                if target > nums[mid] and target <= nums[right]:
                    # there is no split in [mid, right]
                    # find target from [mid+1, right]
                    left = mid + 1
                    continue
                else:
                    # target will be within [left, mid - 1]
                    right = mid - 1
                    continue

            # there is a split point within (mid, right]
            if nums[mid] > nums[right]:
                # [2,3,4,0,1]
                if target < nums[mid] and target >= nums[left]:
                    # there is no split within [left, mid]
                    # and target is within [left, mid]. For instance target = 3
                    right = mid - 1
                    continue
                else:
                    # target is within [mid+1, right], For instance target = 1
                    left = mid + 1
                    continue

            # this is a normal range, without splitting point
            # [2,3,4], a sub array of original [2,3,4,0,1]
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # cannot find the target
        return -1