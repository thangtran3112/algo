from typing import List
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 3 4 5
        # left:  1    2    6   24  120 (left[i] = left[i - 1] * nums[i])
        # right: 120  120  60  20  5
        # answer[i] = left[i - 1] * right[i + 1] if left[i - 1] or right[i + 1] present
        left = [1] * len(nums)
        right = [1] * len(nums)
        answers = [1] * len(nums)
        left[0] = nums[0]
        right[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i]

        for i in range(len(nums)):
            if i == 0:
                answers[0] = right[1]
                continue
            if i == len(nums) - 1:
                answers[i] = left[len(nums) - 2]
                break
            answers[i] = left[i - 1] * right[i + 1]

        return answers