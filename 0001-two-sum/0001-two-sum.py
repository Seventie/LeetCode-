class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}      
        for i in range(len(nums)):
            left = target - nums[i]      
            if left in storage:
                return [storage[left], i]   
            storage[nums[i]] = i  
        return []