class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        moves =[
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        def dfs(x, y) :
            if x < 0 or y < 0 or x >= n or y >= m or grid[x][y] != '1' :
                return 
            grid[x][y] = '#'
            for dx, dy in moves :
                dfs(x+ dx, y+ dy)
        ans = 0 
        for x in range(n):
            for y in range(m):
                if grid[x][y] == '1':
                    dfs(x,y)
                    ans += 1
        return ans 