class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        ## Tryna code all by myself here
        ## Using the Disjoint sets and all those stuff

        disjoint_sets = {}

        code = [ord('a')]

        n = len(grid)
        m = len(grid[0])

        moves = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]
        def search(x, y):
            seen = set()
            _m = 0
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    val = grid[nx][ny]
                    if val != 0 and val not in seen:
                        seen.add(val)
                        _m += disjoint_sets[val]
            return 1 + _m
        def dfs(x, y, mark):
            if x < 0 or y < 0 or y >= m or x >= n or grid[x][y] != 1:
                return 0
            grid[x][y] = mark
            res = 1
            for dx, dy in moves:
                res += dfs(x + dx, y + dy, mark)
            return res
        ## preprocessing islands
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 1:
                    mark = chr(code[0])
                    size = dfs(x, y, mark)
                    disjoint_sets[mark] = size
                    code[0] += 1
        ans = 0
        f = False
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 0:
                    ans = max(ans, search(x, y))
                    f = True
        if not f:
            return n * n
        return ans