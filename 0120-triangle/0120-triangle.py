class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = triangle[-1][:]  
        for i in range(len(triangle) - 2, -1, -1):
            curr = [0] * len(triangle[i])
            for j in range(len(curr)):
                curr[j] = min(prev[j], prev[j+1]) + triangle[i][j]
            prev = curr
        
        return prev[0]