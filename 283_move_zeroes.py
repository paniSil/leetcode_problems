# 283. Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: list[int]) -> list:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = nums.count(0)

        nums[:] = (n for n in nums if n != 0)

        nums += [0]*counter


class Solution2:
    def moveZeroes(self, nums: list[int]) -> list:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = nums.count(0)

        while 0 in nums:
            nums.remove(0)

        nums += [0]*counter
