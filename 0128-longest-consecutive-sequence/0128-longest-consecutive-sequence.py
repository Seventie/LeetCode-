class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  
        if not nums :
            return 0
        n = set(nums)
        maxi = 0 
        for x in n :
            if x-1 not in n :
                current = x 
                c = 1 
                while current+1 in n :
                    c += 1
                    current += 1
                maxi = max(maxi,c)
        return maxi

        
