class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1 : return 1 
        n = len(ratings)
        dp = [1] * n 

        for x in range(1,n)  :
            if ratings[x] > ratings[x-1] :
                dp[x] = dp[x-1] + 1

        for x in range(n-2,-1,-1)  :
            if ratings[x] > ratings[x+1] :
                dp[x] = max(dp[x],dp[x+1] + 1)
        
        return sum(dp)