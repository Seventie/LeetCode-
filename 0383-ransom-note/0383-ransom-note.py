class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = [0] * 26
        for x in magazine :
            a[ord(x)- ord('a')] += 1
        for x in ransomNote :
            if a[ord(x) - ord('a')] >0 :
                a[ord(x) - ord('a')] -= 1
            else :
                return False 
        return True 