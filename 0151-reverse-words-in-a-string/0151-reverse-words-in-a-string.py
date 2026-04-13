class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = ""
        for x in s :
            ans = x + " " + ans 
        return ans.strip()
