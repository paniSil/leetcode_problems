# 151. Reverse Words in a String


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        s = ' '.join(s)
        return s
