class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= k:
            return sum(nums) / k
        csum = 0
        for i in range(k):
            csum += nums[i]
        _max = csum
        for i in range(k, len(nums)):
            csum += nums[i] - nums[i - k]
            _max = max(_max, csum)
        return _max / k