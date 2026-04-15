class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tot = 0
        prev = nums[0]
        ans = 0
        for x in range(k) :
            ans += nums[x]
        tot = ans  
        for x in range(k,len(nums)):
            prev = nums[x - k]
            tot = tot + nums[x] - prev  
            ans = max(ans ,tot)
        return ans 
