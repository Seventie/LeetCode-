# # Approach
# My approach was just oing directly into the problem using a for loop and tracker that tracks the current index of the new value to be inserted at .

# # Complexity
# - Time complexity:
# O(n)

# - Space complexity:
# O(n)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tracker = 0 
        for x in range(len(nums)):
            if nums[x]!= val :
                nums[tracker] = nums[x]
                tracker+=1
        return tracker 


