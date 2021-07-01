# Remove Duplicates from Sorted Array https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# * Must have O(1) extra memory allocation. (Not allowed to create new lists)
# https://leetcode.com/submissions/detail/515604837/


def removeDuplicates(nums: list[int]) -> int:
    for i, n in enumerate(nums):
        for m in nums[i + 1 : :]:
            if n == m:
                nums.pop(i)

    return len(nums)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums), nums)
nums = [1, 1, 2]
print(removeDuplicates(nums), nums)
