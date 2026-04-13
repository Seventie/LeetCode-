class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        
        for x in range(len(nums)):
            # skip duplicate fixed elements
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            
            fix = nums[x]
            i, j = x + 1, len(nums) - 1
            
            while i < j:
                tot = nums[i] + nums[j]
                
                if tot == -fix:
                    ans.append([fix, nums[i], nums[j]])
                    
                    i += 1
                    j -= 1
                    
                    # skip duplicates
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                
                elif tot < -fix:
                    i += 1
                else:
                    j -= 1
        
        return ans