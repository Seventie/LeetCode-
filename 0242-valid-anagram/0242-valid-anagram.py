class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  
        a = [0] * 26
        for x in s:
            idx = ord(x) - ord('a')
            a[idx] += 1
        for x in t:
            idx = ord(x) - ord('a')
            if a[idx] == 0:
                return False
            a[idx] -= 1
        return True