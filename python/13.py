# Roman to Integer https://leetcode.com/problems/roman-to-integer/
# https://leetcode.com/submissions/detail/514193503/
def romanToInt(s: str) -> int:
    map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    sum = 0
    prev = None
    for c in s:
        if prev:
            # Check for combos
            if prev == "I" and c == "V":
                sum += 4
                prev = None
            elif prev == "I" and c == "X":
                sum += 9
                prev = None
            elif prev == "X" and c == "L":
                sum += 40
                prev = None
            elif prev == "X" and c == "C":
                sum += 90
                prev = None
            elif prev == "C" and c == "D":
                sum += 400
                prev = None
            elif prev == "C" and c == "M":
                sum += 900
                prev = None
            else:
                # Not a combo, add previous
                sum += map[prev]
                prev = c
        elif c in ["I", "X", "C"]:
            # Potential combo
            prev = c
        else:
            sum += map[c]
            prev = None

    # Handle final character if needed
    if prev:
        sum += map[prev]

    return sum


print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
print(romanToInt("MDCCCLXXXIV"))
