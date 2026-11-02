
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums=[-i for i in nums]
        heapq.heapify(nums)
        for j in range(0,k):
            r=-(heapq.heappop(nums))
        return r



        