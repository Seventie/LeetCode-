class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0 
        s = s.strip()
        s = list(s)
        print(s)
        while s:
            if s[-1] == ' ':
                return ans 
            else :
                ans += 1
            s.pop()
        return ans 