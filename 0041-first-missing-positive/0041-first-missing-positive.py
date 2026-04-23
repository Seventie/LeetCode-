class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for x in range(n):
            while 1 <= nums[x] <= n and nums[x] != nums[nums[x] - 1] :
                idx = nums[x] - 1
                nums[idx],nums[x] = nums[x],nums[idx]
        for x in range(n):
            if nums[x] != x + 1:
                return x + 1
        return n + 1