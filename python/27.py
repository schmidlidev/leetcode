# Remove Element https://leetcode.com/problems/remove-element/
# * Must have O(1) extra memory allocation. (Not allowed to create new lists)
# https://leetcode.com/submissions/detail/515610034/


def removeElement(nums: list[int], val: int) -> int:
    while val in nums:
        nums.remove(val)

    return len(nums)


nums = [0, 1, 2, 2, 3, 0, 4, 2]
print(removeElement(nums, 2), nums)
