class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        csum = 0 
        mp = {0 : 1}
        ans = 0 

        for num in nums :
            csum += num 
            rem = csum % k 

            if rem in mp :
                ans += mp[rem]  
                mp[rem] += 1
            else :
                mp[rem] = 1
        
        return ans 