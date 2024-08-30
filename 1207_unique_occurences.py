# 1207. Unique Number of Occurrences
# Link: https://leetcode.com/problems/unique-number-of-occurrences/


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        collection = {}

        for n in arr:
            collection[n] = collection.get(n, 0) + 1

        if len(list(collection.values())) == len(set(collection.values())):
            return True
        else:
            return False
