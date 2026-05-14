class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n
        p1 = 3
        p2 = 2
        cur = 0

        for _ in range(3, n):
            cur = p1 + p2
            p2 = p1
            p1 = cur
        
        return cur