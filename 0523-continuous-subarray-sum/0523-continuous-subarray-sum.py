class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        csum = 0 
        mp = {0 : -1}

        for x in range(len(nums)) :
            csum += nums[x]
            rem = csum % k 

            if rem in mp :
                if x - mp[rem] >= 2 :
                    return True 
            else :
                mp[rem] = x
            
        return False