class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        i = 0 
        while i < len(nums) :
            if nums[i] > 0 :
                break
            i += 1
        j = i - 1
        k = 0
        while j > -1 or i < len(nums) :
            if j > -1 and i < len(nums):
                if abs(nums[j]) < nums[i] :
                    ans[k] = nums[j]*nums[j]
                    j -= 1
                else :
                    ans[k] = nums[i]*nums[i]
                    i += 1
            elif j < 0 :
                ans[k] = nums[i]*nums[i]
                i += 1 
            else :
                ans[k] = nums[j]*nums[j]
                j -= 1
            k += 1
        
        return ans 