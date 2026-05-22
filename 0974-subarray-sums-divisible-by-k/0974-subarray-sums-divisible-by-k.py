class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        _rem = {0 : 1}
        csum = 0 
        ans = 0 
        for x in nums :
            csum += x 
            rem = csum % k 
            if rem in _rem :
                ans += _rem[rem]
                _rem[rem] += 1
            else :
                _rem[rem] = 1

        return ans 
