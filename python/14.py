# Longest Common Prefix https://leetcode.com/problems/longest-common-prefix/
# https://leetcode.com/submissions/detail/514199938/
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    prefix = ""
    for tup in zip(*strs):
        if len(set(tup)) > 1:
            break
        else:
            prefix += tup[0]

    return prefix
