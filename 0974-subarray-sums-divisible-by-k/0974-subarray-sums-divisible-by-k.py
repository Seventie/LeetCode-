class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0 
        psum = 0 
        pmap = {0 : 1}
        for x in nums :
            psum += x 
            rem = psum % k   
            if rem in pmap :
                ans += pmap[rem]
            if rem in pmap :
                pmap[rem] += 1
            else :
                pmap[rem] = 1 

        return ans