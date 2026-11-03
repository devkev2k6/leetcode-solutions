import heapq

class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        
        max_heap = [-p for p in piles]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            largest = -heapq.heappop(max_heap)
           
            remaining = largest - (largest // 2)
            heapq.heappush(max_heap, -remaining)
            
        return -sum(max_heap)