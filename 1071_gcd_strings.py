# 1071. Greatest Common Divisor of Strings


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            a = len(str1)
            b = len(str2)
            divider = min (a, b)
            while divider > 0:
                if a % divider == 0 and b % divider == 0:
                    res = str1[:divider]
                    break
                divider -= 1
            return res
        else:
            return ''
