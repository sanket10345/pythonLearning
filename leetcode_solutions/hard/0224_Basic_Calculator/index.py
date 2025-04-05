"""
LeetCode Problem 224: Basic Calculator
"""

def is_integer(val):
    if isinstance(val, int):
        return True
    elif isinstance(val, str):
        return val.strip().lstrip('-').isdigit()
    else:
        return False

def parse_int_if_possible(s):
    try:
        return int(s)
    except ValueError:
        return s

def calculate(s):
    s = s.replace(" ", "")
    stack = []
    i = 0

    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            stack.append(num)
            continue

        if s[i] == ')' and stack:
            num = 0
            while stack and stack[-1] != '(':
                # Ensure there are at least 2 elements for safe access
                if len(stack) >= 2 and is_integer(stack[-1]) and stack[-2] == '(':
                    num += stack.pop()
                    stack.pop()  # Remove '('
                    break
                elif len(stack) >= 2 and is_integer(stack[-1]) and stack[-2] in ('+', '-'):
                    op = stack.pop(-2)
                    val = stack.pop()
                    if op == '+':
                        num += val
                    elif op == '-':
                        num -= val
                else:
                    break  # malformed case
            # Remove stray '(' if still there
            if stack and stack[-1] == '(':
                stack.pop()
            stack.append(num)
            i += 1
            continue

        stack.append(parse_int_if_possible(s[i]))
        i += 1

    # Final flat stack evaluation (left to right)
    result = 0
    sign = 1
    while stack:
        token = stack.pop(0)
        if token == '+':
            sign = 1
        elif token == '-':
            sign = -1
        else:
            result += sign * int(token)
    return result

