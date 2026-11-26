class Solution:
    def canAliceWin(self, n: int) -> bool:
        return round(sqrt(110 - 2 * n)) % 2 == 1