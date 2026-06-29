class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        pacific = set()
        atlantic = set()
        def dfs(x, y, seen):
            seen.add((x, y))
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (0 <= nx < n and 0 <= ny < m and
                    (nx, ny) not in seen and
                    heights[nx][ny] >= heights[x][y]):
                    dfs(nx, ny, seen)
        for i in range(n):
            dfs(i, 0, pacific)
        for j in range(m):
            dfs(0, j, pacific)
        for i in range(n):
            dfs(i, m - 1, atlantic)
        for j in range(m):
            dfs(n - 1, j, atlantic)
        return [[x, y] for (x, y) in pacific & atlantic]