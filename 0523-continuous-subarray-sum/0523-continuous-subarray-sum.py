class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False 
        j = 0
        psum = 0
        pmap = {0: -1}   
        while j < len(nums):
            psum += nums[j]
            rem = psum % k
            if rem in pmap:
                if j - pmap[rem] >= 2:   
                    return True
            else:
                pmap[rem] = j 
            j += 1
            
        return False