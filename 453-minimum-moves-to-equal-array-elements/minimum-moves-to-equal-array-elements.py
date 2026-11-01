class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n=len(nums)
        return sum(nums)-(n*min(nums))
        