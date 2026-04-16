class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p) :
            return []
        parr = [0]*26 
        sarr = [0]*26
        for x in p :
            parr[ord(x)-97] += 1
        ans = []
        for x in range(len(s)):
            sarr[ord(s[x])-97] += 1
            if x >= len(p) :
                sarr[ord(s[x-len(p)])-97] -= 1
            if sarr == parr :
                ans.append(x+1-len(p))
        return ans 