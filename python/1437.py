# 1437. Check If All 1's Are at Least Length K Places Away https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/submissions/
# https://leetcode.com/submissions/detail/539667733/
from typing import List


def kLengthApart(nums: List[int], k: int) -> bool:
    distance = k
    for n in nums:
        if n == 1:
            if distance < k:
                return False
            else:
                distance = 0
        else:
            distance += 1

    return True


print(kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2), "|", True)
print(kLengthApart([1, 0, 0, 1, 0, 1], 2), "|", False)
print(kLengthApart([1, 1, 1, 1, 1], 0), "|", True)
print(kLengthApart([0, 1, 0, 1], 1), "|", True)
