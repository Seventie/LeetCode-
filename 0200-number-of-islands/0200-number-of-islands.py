class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        moves = [[-1,0],[0,-1],[1,0],[0,1]]
        def dfs(x, y):
            if x < 0 or y < 0 or x >= n or y >= m or grid[x][y] != "1":
                return
            grid[x][y] = "#"
            for dx, dy in moves:
                dfs(x + dx, y + dy)
        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        return islands
                