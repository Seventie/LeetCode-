class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = _max = _min = nums[0]
        for num in nums[1:] :
            old = _max 
            _max = max(num ,_max*num ,_min*num)
            _min = min(num ,_min*num ,old*num)
            ans = max(_max ,ans)
        return ans 