# 1. Two Sum
# Link: https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:    
        res = []

        for n in nums:
            i = nums.index(n)
            numscheck = nums[:i] + nums[i + 1:]
            ex = target - n
            if ex in numscheck:
                res.append(nums.index(n))
                res.append(numscheck.index(ex)+1)
                break
            else:
                continue
        return res
