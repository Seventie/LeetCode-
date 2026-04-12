class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for x in s :
            if (x.isalpha() or x.isdigit()):
                st += x.lower()
        i = 0 
        j = len(st) -1 
        while i < j :
            if st[i] == st[j]:
                i+=1
                j-=1
            else :
                return False 
        return True 