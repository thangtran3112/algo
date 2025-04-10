# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # https://leetcode.com/explore/learn/card/binary-search/135/template-iii/936/
        # [5,7,7,8,8,8] and [5,7,7,8,8,10] and target=8
        # left=0, right= 5, mid = 2, nums[mid] = 7
        # left=2, right=5, mid = 3, nums[mid] = 8
        # left=3, right=5, mid = 4, nums[mid] = 8
        # exit with left=4, right=5.
        # the rightmost will be either 4 or 5
        def findRightMost():
            left = 0
            right = len(nums) - 1
            while left < right - 1:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    # mid is equal or less than target
                    left = mid
            # this template will have 2 elements to return
            # Post-processing
            if 0 <= right < len(nums) and nums[right] == target:
                return right
            if 0 <= left < len(nums) and nums[left] == target:
                return left
            return -1

        # similar logics
        # https://leetcode.com/explore/learn/card/binary-search/135/template-iii/936/
        def findLeftMost():
            left = 0
            right = len(nums) - 1
            while left < right - 1:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    # mid is equal or higher than target
                    right = mid
            # this template will have 2 elements to return
            if 0 <= left < len(nums) and nums[left] == target:
                return left
            if 0 <= right < len(nums) and nums[right] == target:
                return right
            return -1

        leftmost = findLeftMost()
        if leftmost == -1:
            return [-1, -1]
        else:
            rightmost = findRightMost()
            return [leftmost, rightmost]