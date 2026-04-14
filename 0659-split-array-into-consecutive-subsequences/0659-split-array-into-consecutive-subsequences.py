class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        tails = defaultdict(int)
        for num in nums:
            if freq[num] == 0:
                continue
            if tails[num] > 0:
                tails[num] -= 1
                tails[num + 1] += 1
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                tails[num + 3] += 1
            else:
                return False
            freq[num] -= 1
        return True
        