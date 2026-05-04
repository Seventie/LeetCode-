class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*m for _ in range(n)]
        if m == 1 or n == 1 :
            return 1 
        for x in range(n-2,-1,-1) :
            for y in range(m-2,-1,-1) :
                dp[x][y] = dp[x+1][y] + dp[x][y+1]
        
        return dp[0][0]