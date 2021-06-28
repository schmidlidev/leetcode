# Palindrome Number https://leetcode.com/problems/palindrome-number/
# https://leetcode.com/submissions/detail/514181366/
def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


# Follow Up: Could you solve it without converting the integer to a string?
# https://leetcode.com/submissions/detail/514185534/
def isPalindromeNoConvert(x: int) -> bool:
    if x < 0:
        return False

    digits = []
    while x != 0:
        digits.append(x % 10)
        x = int(x / 10)

    print(digits)
    for i, digit in enumerate(digits):
        if digit != digits[len(digits) - i - 1]:
            return False

    return True
