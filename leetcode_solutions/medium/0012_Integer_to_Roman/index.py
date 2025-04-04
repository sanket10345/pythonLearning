"""
LeetCode Problem 12: Integer to Roman
"""

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    number_to_roman = [
        (1000,'M'),
        (900,'CM'),
        (500,'D'),
        (400,'CD'),
        (100,'C'),
        (90,'XC'),
        (50,'L'),
        (40,'XL'),
        (10,'X'),
        (9,'IX'),
        (5,'V'),
        (4,'IV'),
        (1,'I')
     ]
    roman =''
    for value, symbol in number_to_roman:
        count = num // value
        roman += symbol * count
        num -= value * count
    return roman
