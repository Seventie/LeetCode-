class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        for x in nums :
            if x != 0 :
                nums[i] = x 
                i += 1
            else :
                pass 
        while i < len(nums) :
            nums[i] = 0 
            i += 1
        return nums 
        