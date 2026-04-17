class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        i = 0 
        ans = 0      
        for j in range(1, len(values)):
            cscore = values[i] + values[j] + i - j
            if values[i] + i <= values[j] + j:
                i = j    
            ans = max(ans, cscore)
        return ans