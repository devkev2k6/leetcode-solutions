class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        answer = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    continue
                stack = [(r,c)]
                grid[r][c] = 1
                closed = True
                while stack:
                    x,y = stack.pop()
                    if x in (0,m-1) or y in (0,n-1):
                        closed = False
                    for xx,yy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                        if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 0:
                            grid[xx][yy] = 1
                            stack.append((xx,yy))
                answer += closed
        return answer
