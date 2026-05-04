class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:   
        if len(matrix) == 1 or not matrix[0]:
            return min(matrix[0])
        n ,m = len(matrix), len(matrix[0])

        if m == 1 :
            ans = 0
            for x in matrix :
                ans += sum(x)
            return ans 

        prev = [0]* m
        curr = [0]* m
        
        for x in range(n) :
            curr[0]  = min(prev[0],prev[1]) + matrix[x][0]
            curr[-1] = min(prev[-1],prev[-2]) + matrix[x][-1]

            for y in range(1,m-1) :
                curr[y] = min(prev[y],prev[y-1],prev[y+1]) + matrix[x][y]
            prev = curr[:]
        return min(curr)