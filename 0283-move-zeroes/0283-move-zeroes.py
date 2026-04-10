class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        i = 0 
        for x in range(len(nums)) :
            if nums[x] == 0 :
                count += 1 
            else :
                nums[i] = nums[x]
                i+=1 
        for x in range(count) :
            nums[i] = 0 
            i+= 1
        