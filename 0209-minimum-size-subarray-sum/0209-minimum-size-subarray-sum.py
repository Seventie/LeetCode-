class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 0
        i = 0
        csum = 0
        for x in range(len(nums)):
            csum += nums[x]
            while csum >= target :
                ans = x+1 if ans == 0 else min(ans,x-i+1)
                csum -= nums[i]
                i += 1 
        return ans
