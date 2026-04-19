
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ones = 0
        ans = 0 
        i = 0 
        for j in range(len(nums)) :
    
            if nums[j] == 1 :
                ones += 1 
            curr = j - i + 1
            if curr - ones > k :
                if nums[i] == 1 :
                    ones -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans 
