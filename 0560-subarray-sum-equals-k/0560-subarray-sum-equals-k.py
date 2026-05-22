class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        _pre = {0 : 1}
        csum = 0 
        ans = 0 
        for x in nums :
            csum += x 
            if csum - k in _pre :
                ans += _pre[csum - k]
            if csum in _pre :
                _pre[csum] += 1
            else :
                _pre[csum] = 1
        
        return ans 