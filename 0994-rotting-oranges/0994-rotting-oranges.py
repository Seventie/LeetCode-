class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        _f = 0 
        q = deque()
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        for x in range(n) :
            for y in range(m):
                if grid[x][y] == 2 :
                    q.append((x,y))
                elif grid[x][y] == 1 :
                    _f += 1
                else : pass 
        ans = 0 
        while q and _f > 0 :
            for x in range(len(q)) :
                cx , cy = q.pop() 
                for dx, dy in moves :
                    nx , ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < m :
                        if grid[nx][ny] == 1 :
                            _f -=1 
                            grid[nx][ny] = 2
                            q.appendleft((nx,ny))
            ans += 1
        return ans if _f == 0 else -1 
