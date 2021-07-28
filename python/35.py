# Search Insert Position https://leetcode.com/problems/search-insert-position/
# https://leetcode.com/submissions/detail/529410388/
from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        pivotIndex = (start + end) // 2
        pivotValue = nums[pivotIndex]

        if target == pivotValue:
            return pivotIndex

        if target < pivotValue:
            end = pivotIndex - 1

        if target > pivotValue:
            start = pivotIndex + 1

    if target <= pivotValue:
        return pivotIndex
    else:
        return pivotIndex + 1


# Actual | Expected
print(searchInsert([1, 3, 5, 6], 5), "|", 2)
print(searchInsert([1, 3, 5, 6], 2), "|", 1)
print(searchInsert([1, 3, 5, 6], 7), "|", 4)
print(searchInsert([1, 3, 5, 6], 0), "|", 0)
print(searchInsert([1], 0), "|", 0)
print(searchInsert([1, 3], 0), "|", 0)
print(searchInsert([1, 3], 4), "|", 2)
