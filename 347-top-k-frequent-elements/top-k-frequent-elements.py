from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)  # Counts frequencies: {num: freq}
        
        # buckets[i] will store all numbers that appear exactly i times
        # Length is len(nums) + 1 because an element can appear up to len(nums) times
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
            
        result = []
        # Traverse from highest frequency down to lowest
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result