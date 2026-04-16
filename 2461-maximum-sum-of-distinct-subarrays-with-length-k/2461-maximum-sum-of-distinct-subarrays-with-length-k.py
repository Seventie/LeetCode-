
class Solution:
    def maximumSubarraySum(self, nums, k):
        if k > len(nums):
            return 0
        ans = 0
        current = deque()
        seen = set()
        csum = 0
        for x in range(len(nums)):
            while nums[x] in seen:
                removed = current.popleft()
                seen.remove(removed)
                csum -= removed
            current.append(nums[x])
            seen.add(nums[x])
            csum += nums[x]
            if len(current) > k:
                removed = current.popleft()
                seen.remove(removed)
                csum -= removed
            if len(current) == k:
                ans = max(ans, csum)

        return ans