# 1952. Three Divisors
# Link: https://leetcode.com/problems/three-divisors/

class Solution:
    def isThree(self, n: int) -> bool:
        m = 1
        devision_counter = 0

        while m <= n:
            devision_result = n % m
            m += 1
            if devision_result == 0:
                devision_counter += 1
            else:
                devision_counter += 0
        if devision_counter == 3:
            return True
        else:
            return False
