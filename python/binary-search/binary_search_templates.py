# https://leetcode.com/explore/learn/card/binary-search/125/template-i/938/
def originalBinarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1

# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/937/
"""
* Use the element's right neighbor to determine if the condition is met and decide whether to go left or right
* Guarantees Search Space is at least 2 in size at each step
* Loop/Recursion ends when you have 1 element left.
"""
def oneElementLeftBinarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if nums[left] == target:
        return left
    return -1

# https://leetcode.com/explore/learn/card/binary-search/135/template-iii/936/
"""
Use the element's neighbors to determine if the condition is met and decide whether to go left or right
Guarantees Search Space is at least 3 in size at each step
Loop/Recursion ends when you have 2 elements left.
"""
def twoElementsBinarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1