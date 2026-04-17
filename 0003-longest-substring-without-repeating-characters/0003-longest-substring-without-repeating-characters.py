class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        ans = 0  
        for x in range(len(s)) :
            if s[x] not in seen :
                seen.add(s[x])
                ans = max(ans ,x-left+1)
            else :
                while s[x] in seen :
                    seen.remove(s[left])
                    left += 1 
                seen.add(s[x])

        return ans 