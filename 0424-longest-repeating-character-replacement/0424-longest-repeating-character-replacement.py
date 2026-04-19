class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)
        i = 0 
        ans = 0 
        for j in range(len(s)):
            mp[s[j]] += 1
            curr = j - i + 1
            _max = max(mp.values())
            if curr - _max > k :
                mp[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans 