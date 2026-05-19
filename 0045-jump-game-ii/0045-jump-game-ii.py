class Solution:
    def jump(self, nums: List[int]) -> int:
        n =  len(nums) 
        dp = n * [float(inf)]
        dp[0] = 0
        for x in range(n) :
            curr = x + nums[x]
            for j in range(x + 1, curr+1) :
                if j < n :
                    dp[j] = min(dp[x] + 1, dp[j])
                else :
                    break
    
        return dp[-1]