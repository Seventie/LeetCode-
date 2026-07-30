class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        store = {}
        ans = 0
        for x in nums :
            if x in store :
                ans += store[x]
                store[x] += 1

            else :
                store[x] = 1
        return ans 