# 151. Reverse Words in a String
# Link: https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        s = ' '.join(s)
        return s
