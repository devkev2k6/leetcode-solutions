class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        minv=float('inf')
        for i in range(0,len(nums),2):
            merged=int(str(nums[i])+str(nums[i+1]))
            minv=min(merged,minv)
        return minv




        