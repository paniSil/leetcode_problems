# 2215. Find the Difference of Two Arrays

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1 = set(nums1) - set(nums2)
        res2 = set(nums2) - set(nums1)
        result = [res1, res2]
        return result
