class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        s=0
        for i in range (len(nums)):
            s+=nums[i]
            nums[i]=s
        return nums

        