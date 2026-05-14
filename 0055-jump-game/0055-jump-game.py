class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fuel = 0 

        for x in nums :
            if fuel < 0 :
                return False 
            if x > fuel :
                fuel = x 
            fuel -= 1 
        return True 