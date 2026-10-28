class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        nums1Idx={num:i for i,num in enumerate(nums1)}
        res=[-1]* len(nums1)

        for i in range (len(nums2)):
            cur=nums2[i]
            while stack and cur>stack[-1]:
                val = stack.pop()
                idx=nums1Idx[val]
                res[idx]=cur
            if cur in nums1Idx:
                    stack.append(cur)
        return res
        