class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        
        dp = [0] * n
        dp[0] = 1 << 0

        for row in grid:
            for c in range(n):
                combined_mask = dp[c] | (dp[c - 1] if c > 0 else 0)
                
                val = row[c]
                next_mask = 0
                while combined_mask:
                    lsb = combined_mask & -combined_mask
                    x = lsb.bit_length() - 1
                    next_mask |= 1 << (x ^ val)
                    combined_mask ^= lsb
                
                dp[c] = next_mask

        target_mask = dp[-1]
        return (target_mask & -target_mask).bit_length() - 1