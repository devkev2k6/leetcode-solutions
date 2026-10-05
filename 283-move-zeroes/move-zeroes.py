class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for r in range(len(nums)):
            if nums[r]!=0:
                nums[l]=nums[r]
                if r!=l:
                    nums[r]=0
                l+=1
                
