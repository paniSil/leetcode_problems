# 345. Reverse Vowels of a String


class Solution:
    def reverseVowels(self, s: str) -> str:
        temp = []
        s = list(s)
        letters = len(s)

        for i in range(letters):
            if s[i].lower() in 'aeiou':
                temp.append(s[i])
                s[i] = '^'
            else:
                continue

        temp.reverse()

        n = 0
        for i in range(letters):
            if s[i] == '^':
                s[i] = temp[n]
                n += 1

        return ''.join(s)
