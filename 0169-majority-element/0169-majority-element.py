class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = None
        cnt = 0
        for x in nums:
            if cnt == 0:
                ele = x
                cnt = 1
            elif x == ele:
                cnt += 1
            else:
                cnt -= 1

        return ele