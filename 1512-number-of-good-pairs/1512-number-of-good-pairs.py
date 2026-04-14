class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        store = defaultdict(int)
        ans = 0 
        for x in nums :
            if store[x] != 0 :
                ans += store[x]
            store[x]+=1
        return ans 