class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        def filler(x, y) :
            if x < 0 or y < 0 or y >= m or x >= n or board[x][y] != 'O' :
                return 
            board[x][y] = "N"
            for dx, dy in dirs :
                filler(x+ dx, y+ dy)
        if n < 2 or m < 2 :
            return board 
        for i in range(n):
            filler(i, 0)       
            filler(i, m - 1)   
        for j in range(m):
            filler(0, j)       
            filler(n - 1, j)  
        for x in range(n):
            for y in range(m) :
                if board[x][y] == "O" :
                    board[x][y] = "X"
                elif board[x][y] == "N" :
                    board[x][y] = "O"
        return board
        