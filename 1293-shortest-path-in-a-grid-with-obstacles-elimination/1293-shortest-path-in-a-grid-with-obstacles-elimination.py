from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        if k >= n + m - 2:
            return n + m - 2
        q = deque([(0, 0, k, 0)])  #
        seen = {(0, 0, k)}
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        while q:
            x, y, rem, steps = q.popleft()
            if x == n - 1 and y == m - 1:
                return steps
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    new_rem = rem - grid[nx][ny]
                    if new_rem >= 0 and (nx, ny, new_rem) not in seen:
                        seen.add((nx, ny, new_rem))
                        q.append((nx, ny, new_rem, steps + 1))
        return -1