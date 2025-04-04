"""
LeetCode Problem 8: String to Integer (atoi)
"""

def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.lstrip()  # Trim leading spaces
    if not s:
        return 0

    num=0
    i=0
    sign=1

    INT_MIN = - 2 ** 31
    INT_MAX = 2 ** 31 -1
    if s[i] in "+-":
        sign = -1 if s[i] == '-' else 1
        i += 1

    while i < len(s) and s[i].isdigit():
        num = num * 10 + int(s[i])
        i+=1
        if sign * num >= INT_MAX:
            return INT_MAX
        if sign * num <= INT_MIN:
            return INT_MIN
    return sign * num

