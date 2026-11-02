class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        target = median_low(nums)
        return sum(abs(num-target) for num in nums)