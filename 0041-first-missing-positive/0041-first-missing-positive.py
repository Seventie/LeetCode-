class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for x in range(length):
            while 1 <= nums[x] <= length and nums[x] != nums[nums[x] - 1]:
                correct_index = nums[x] - 1
                nums[x], nums[correct_index] = nums[correct_index], nums[x]
        for x in range(length):
            if nums[x] != x + 1:
                return x + 1
        return length + 1
    
                


        # [0,1,2,3] (4)
        # [1,2,3,4]