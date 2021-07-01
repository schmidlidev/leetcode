# Implement strStr() https://leetcode.com/problems/implement-strstr/
# https://leetcode.com/submissions/detail/515657533/


def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    if len(needle) > len(haystack):
        return -1

    for i in range(0, len(haystack)):
        for j, c in enumerate(needle):
            if i + len(needle) > len(haystack):
                return -1
            if c != haystack[i + j]:
                break
            elif j == len(needle) - 1:
                return i

    return -1


print(strStr("hello", "ll"))
print(strStr("aaa", "aaa"))
print(strStr("baa", "ca"))
print(strStr("mississippi", "issipi"))
print(strStr("a", "a"))
