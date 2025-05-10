# https://leetcode.com/problems/kth-missing-positive-number
"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
 

Follow up:

Could you solve this problem in less than O(n) complexity?
"""
import pytest
class Solution:
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # Example:    [2, 3, 4, 7, 11, 15] , k = 4
        # Not miss:   [1, 2, 3, 4, 5,   6]
        # Count_miss: [1, 1, 1, 3, 6,   9]
        # Recipe: miss[index] = arr[index] - index - 1
        # Binary search miss between Count_miss, so miss = k or miss is nearest to k
        # In this example, miss = (index=3, value=7), as it is just behind k = 4
        # At 7, we miss 3 positive integer, so to get Kth missed, we need 7 + (k - missAt7)
        # Notes: for this Binary Search, we will try to return mid or left
        def get_miss(index):
            return arr[index] - index - 1
        
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            # Otherwise, go left.
            else:
                right = mid - 1
        
        # At the end of the loop, left = right
        if get_miss(left) < k:
            left += 1
        # and the kth missing is in-between arr[left - 1] and arr[left].
        # (left - 1) is the possition just smaller missing than k
        # missing element = arr[left - 1] + k - get_miss(left - 1)
        return arr[left - 1] + k - get_miss(left - 1)
    
