class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for x in s :
            if (x.isalpha() or x.isdigit()):
                st += x.lower()
        i = 0 
        j = len(st) -1 
        
        return st == st[::-1]