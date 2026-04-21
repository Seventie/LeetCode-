class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        a = nums
        def perm(i):
            if i == len(a) :
                ans.append(a[:])
                return 
            for j in range(i,len(a)):
                a[i],a[j] =a[j],a[i]
                perm(i + 1)
                a[i],a[j] =a[j],a[i]

        perm(0)
        return ans 