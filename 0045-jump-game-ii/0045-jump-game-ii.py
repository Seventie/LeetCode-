class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float(inf)] * len(nums)
        dp[0] = 0
        for x in range(len(nums)) :
            curr = nums[x]
            for i in range(x+1,x+curr+1) :
                if i < len(nums) :
                    dp[i] = min(dp[x] + 1 , dp[i])
                else :
                    break

        return dp[-1]