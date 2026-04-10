class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        map = defaultdict(int)
        for x in nums :
            map[x]+= 1 
            if map[x] > length/2 :
                return x 
        