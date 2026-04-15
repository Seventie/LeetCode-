class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int :
        count = 0 
        pre_sum = 0 
        pre_sum_mp = {0 : 1}
        for x in nums :
            pre_sum += x 
            if (pre_sum - k) in pre_sum_mp :
                count += pre_sum_mp[pre_sum - k]
            if pre_sum in pre_sum_mp :
                pre_sum_mp[pre_sum] += 1
            else :
                pre_sum_mp[pre_sum] = 1
        return count 