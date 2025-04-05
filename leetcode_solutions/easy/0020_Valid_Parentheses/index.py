"""
LeetCode Problem 20: Valid Parentheses
"""

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack=[]
    i=0
    pairs={
        ')':'(',
        '}':'{',
        ']':'[',
    }
    for char in s:
        if char in ['(','{','[']:
          stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            continue
    return len(stack) == 0


