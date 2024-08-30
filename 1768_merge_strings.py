# 1768. Merge Strings Alternately
# Link: https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1 = 0
        i2 = 0
        i1_max = len(word1)
        i2_max = len(word2)
        result = ''
        while len(result) <= len(word1) + len (word2):
            if i1 < i1_max and i2 < i2_max:
                result = result + (word1[i1]) + (word2[i2])
                i1 += 1
                i2 += 1
            else:
                break

            word1_left = word1[len(word1) - (len(word1)-i1):]
            word2_left = word2[len(word2) - (len(word2)-i2):]

            fin_result = result + word1_left + word2_left
        return fin_result
