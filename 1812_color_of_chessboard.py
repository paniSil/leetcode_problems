# 1812. Determine Color of Chessboard Square
# Link: https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        first = coordinates[0]
        second = int(coordinates[1])
        if second % 2 == 0:
            if first == 'a' or first == 'c' or first == 'e' or first == 'g':
                return True
            else:
                return False
        else:
            if first == 'b' or first == 'd' or first == 'f' or first == 'h':
                return True
            else:
                return False
