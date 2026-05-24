class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        moves = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or board[x][y] != 'O':
                return
            board[x][y] = '@'
            for dx, dy in moves:
                dfs(x + dx, y + dy)
        for y in range(m):
            dfs(0, y)
            dfs(n - 1, y)
        for x in range(n):
            dfs(x, 0)
            dfs(x, m - 1)
        for x in range(n):
            for y in range(m):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == '@':
                    board[x][y] = 'O'