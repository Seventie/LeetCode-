class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(n):
            for jump in range(1, nums[i] + 1):
                nxt = i + jump
                if nxt < n:
                    dp[nxt] = min(dp[nxt], dp[i] + 1)
        return dp[-1]