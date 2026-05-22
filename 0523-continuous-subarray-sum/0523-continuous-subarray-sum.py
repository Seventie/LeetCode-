class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        _rem = {0 : -1}
        csum = 0 
        ans = False 
        for x in range(len(nums)) :
            csum += nums[x] 
            rem = csum % k 
            if rem in _rem :
                if x - _rem[rem] > 1 :
                    return True 
            else :
                _rem[rem] = x
        return False 