class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height) -1 
        max_water = min(height[i],height[j])* (j-i)
        while i < j :
            capacity = 0
            if height[i] < height[j] :
                capacity = height[i]* (j-i)
                i+=1
            else :
                capacity = height[j]* (j-i)
                j -= 1 
            max_water = max(capacity,max_water)
        return max_water
