class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        dp = [float("inf")] * n 
        dp[0] = 0
        for x in range(n) :
            curr = nums[x]
            j = x + 1
            while j < n and j <= x + curr:
                dp[j] = min(dp[j],dp[x]+1)
                j += 1
        return dp[-1]
            