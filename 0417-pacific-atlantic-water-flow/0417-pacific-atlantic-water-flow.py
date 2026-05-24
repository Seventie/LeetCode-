class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacific = set()
        atlantic = set()
        moves = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        def dfs(x, y, visited):
            visited.add((x, y))
            for dx, dy in moves:
                nx, ny = x + dx, y + dy

                if (
                    0 <= nx < n and
                    0 <= ny < m and
                    (nx, ny) not in visited and
                    heights[nx][ny] >= heights[x][y]
                ):
                    dfs(nx, ny, visited)
        for y in range(m):
            dfs(0, y, pacific)
            dfs(n - 1, y, atlantic)
        for x in range(n):
            dfs(x, 0, pacific)
            dfs(x, m - 1, atlantic)
        ans = []
        for cell in pacific & atlantic:
            ans.append(list(cell))
        return ans