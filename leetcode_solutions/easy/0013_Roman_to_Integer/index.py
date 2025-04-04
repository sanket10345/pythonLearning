def romanToInt(s):
   roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
   sum = 0
   prevValue = roman[s[0]]
   
   for i in range(1, len(s)):
       currentValue = roman[s[i]]
       sum += -prevValue if (currentValue > prevValue) else prevValue
       prevValue = currentValue
   sum += prevValue
   return sum