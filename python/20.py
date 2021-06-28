# Valid Parentheses https://leetcode.com/problems/valid-parentheses/
# https://leetcode.com/submissions/detail/514204474/
def isValid(s: str) -> bool:
    def sibling(c):
        if c == "(":
            return ")"
        if c == "{":
            return "}"
        if c == "[":
            return "]"

    stack = []
    for c in s:
        if c in ["(", "{", "["]:
            stack.append(c)
        else:
            # If stack is empty then there is a closing brace without an opening one.
            if not stack:
                return False
            if c != sibling(stack.pop()):
                return False

    if stack:
        return False

    return True


print(isValid("()"))  # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))  # False
print(isValid("([)]"))  # False
print(isValid("{[]}"))  # True
