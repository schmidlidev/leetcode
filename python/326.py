# 326. Power of Three https://leetcode.com/problems/power-of-three/
# https://leetcode.com/submissions/detail/539637521/


def isPowerOfThree(n: int) -> bool:
    if n == 1:
        return True

    if n <= 0:
        return False

    quotient, remainder = divmod(n, 3)
    if remainder == 0:
        return isPowerOfThree(quotient)
    else:
        return False


print(isPowerOfThree(27), "|", True)
print(isPowerOfThree(0), "|", False)
print(isPowerOfThree(9), "|", True)
print(isPowerOfThree(45), "|", False)
print(isPowerOfThree(-3), "|", False)
