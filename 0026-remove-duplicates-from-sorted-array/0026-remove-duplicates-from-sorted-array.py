class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0 
        x = 0
        while x < n  :
            curr = nums[x]
            nums[i] = curr
            while x + 1 < n and nums[x] == nums[x+1] :
                x = x + 1
            x += 1
            i += 1
        return i 
