class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 0
        i = 0 
        csum = 0
        for j in range(len(nums)):
            csum += nums[j]
            if csum >= target :
                while csum-nums[i] >= target :
                        csum -= nums[i]
                        i += 1
                if ans == 0 :
                    ans = j - i + 1
                else :
                    ans = min(ans,j - i + 1)
        return ans 

