class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        def helper(x, y) :
            if x < 0 or y < 0 or y >= m or x >= n or grid[x][y] != '1' :
                return 
            grid[x][y] = '2'
            for dx, dy in dirs :
                helper(x + dx, y+ dy)
        ans = 0
        for x in range(n):
            for y in range(m) :
                if grid[x][y] == '1' :
                    ans += 1
                    helper(x, y)
        return ans 