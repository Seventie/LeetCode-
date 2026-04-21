class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        csum = 0 
        ans = 0 
        mp = {0:1}

        for x in nums :
            csum += x
            rem = csum % k
            
            if rem in mp :
                ans += mp[rem]
            if rem in mp :
                mp[rem] += 1 
            else :
                mp[rem] = 1

        return ans 
