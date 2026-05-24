class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        _q = deque()
        n , m = len(mat), len(mat[0])
        _max = m*n
        moves = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        for x in range(n) :
            for y in range(m) :
                if mat[x][y] == 0 :
                    _q.append((x,y))
                else :
                    mat[x][y] = _max
        while _q :
            cx, cy = _q.popleft()
            for dx, dy in moves :
                nx, ny = cx+ dx, cy +dy 
                if 0 <= nx < n and 0 <= ny < m and mat[cx][cy] < mat[nx][ny] :
                    mat[nx][ny] = mat[cx][cy] + 1
                    _q.append((nx,ny))
        return mat 