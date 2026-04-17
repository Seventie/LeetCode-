class Solution:
    def maxSubarraySumCircular(self, nums):
        currSum = 0
        maxSum = float('-inf')
        for num in nums:
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, currSum)
        currSum = 0
        minSum = float('inf')
        for num in nums:
            currSum = min(num, currSum + num)
            minSum = min(minSum, currSum)
        totalSum = sum(nums)
        maxCircular = totalSum - minSum
        if maxSum > 0:
            return max(maxSum, maxCircular)
        return maxSum