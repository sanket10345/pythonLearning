"""
LeetCode Problem 67: Add Binary
"""

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    i = len(a) - 1
    j = len(b) - 1
    carryOver = 0
    result = ""

    while i >= 0 or j >= 0 or carryOver:
        bit1 = int(a[i]) if i >= 0 else 0  # Get bit from a or 0 if i < 0
        bit2 = int(b[j]) if j >= 0 else 0  # Get bit from b or 0 if j < 0
        
        total = bit1 + bit2 + carryOver  # Sum of both bits and carry
        
        result = str(total % 2) + result  # Append the binary result (0 or 1)
        carryOver = total // 2  # Carry for next iteration
        
        i -= 1
        j -= 1

    return result

