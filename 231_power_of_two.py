# 231. Power of Two
# Link: https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        counter = 0
        if n == 1:
            return True
        elif n < 1:
            return False
        while n > 1:
            if n % 2 == 0:
                n = n // 2
                counter += 0
            else:
                counter += 1
                break
        if counter == 0:
            return True
        else:
            return False
