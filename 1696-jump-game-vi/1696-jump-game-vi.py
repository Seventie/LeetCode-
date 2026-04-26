class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dq = deque([0])
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + dp[dq[0]]

            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            dq.append(i)

            if dq[0] <= i - k:
                dq.popleft()

        return dp[-1]