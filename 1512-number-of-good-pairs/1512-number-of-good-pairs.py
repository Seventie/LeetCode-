class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        store = Counter(nums)
        ans = 0
        for x in store.values() :
            if x != 1 :
                ans += math.comb(x, 2)

        return ans 