# 1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        res = []
        counter = 0
        while counter < len(candies):
            candies_new = candies[counter] + extraCandies
            if candies_new >= max(candies):
                res.append(True)
            if candies_new < max(candies):
                res.append(False)
            counter += 1
        return res
