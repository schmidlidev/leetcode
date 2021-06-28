#  Reverse Integer https://leetcode.com/problems/reverse-integer/
# * Used references :(
# https://leetcode.com/submissions/detail/514122747/
def reverse(x):

    INT_MAX = (2 ** 31) - 1

    negative = x < 0
    if negative:
        x *= -1

    reversed = 0
    while x != 0:
        digit = x % 10
        x = int(x / 10)

        if reversed > int(INT_MAX / 10) or (
            reversed == int(INT_MAX / 10) and digit > 7 + int(negative)
        ):
            return 0

        reversed *= 10
        reversed += digit

    if negative:
        return reversed * -1

    return reversed


print(reverse(-8463847412))
