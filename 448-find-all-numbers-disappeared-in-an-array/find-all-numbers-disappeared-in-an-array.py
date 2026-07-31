class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        set_nums=set(nums)
        c=[]
        for i in range(1,n+1):
            if i not in set_nums:
                c.append(i)
        return c
         







        