class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -10001
        csum = 0

        for x in nums :
            csum += x 
            ans = max(ans, csum)
            if csum < 0 :
                csum = 0 
        return ans