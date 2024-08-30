# 2215. Find the Difference of Two Arrays
# Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        res1 = set(nums1) - set(nums2)
        res2 = set(nums2) - set(nums1)
        result = [res1, res2]
        return result
