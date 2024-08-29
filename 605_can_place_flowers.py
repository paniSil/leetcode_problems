# 605. Can Place Flowers


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = len(flowerbed)
        res = 0

        if flowers > 1:
            for i in range(flowers):
                if flowerbed[0] == flowerbed[1] == 0:
                    res += 1
                    flowerbed[0] += 1
                elif flowerbed[i] == flowerbed[i-1] == flowerbed[i+1] == 0:
                    res += 1
                    flowerbed[i] += 1
                elif flowerbed[-1] == flowerbed[-2] == 0:
                    res += 1
                    flowerbed[-1] += 1
                else:
                    continue
        else:
            if flowerbed[0] == 0:
                res += 1

        return res >= n
