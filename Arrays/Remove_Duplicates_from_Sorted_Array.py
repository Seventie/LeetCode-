# # Intuition
# I was thinking of two whiole loops when i saw the roblem using pointers

# # Approach
# I basically Have a outerloop in here that acts as if we are traversing as well as an inner loop that checks for the reapeating elemnts and skips them

# # Complexity
# - Time complexity:
# O(n)

# - Space complexity:
# O(n)

# Code
# ```python3 []
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tracker = 0
        x = 0
        while x < len(nums):
            now = nums[x]
            nums[tracker] = now
            while ( x+1 < len(nums) and nums[x+1] == now):
                x+=1
                pass
            tracker+=1
            x+=1
        return tracker 

