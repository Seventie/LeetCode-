class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s :
            return True 
        i = 0 
        for x in t :
            if s[i] == x :
                i += 1 
            if len(s) == i :
                return True 
        return False 