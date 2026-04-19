class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        T = [0] * 128
        for x in t:
            T[ord(x)] += 1
        
        required = len(t)   # 🔥 total chars we still need
        i = 0
        ans = ""
        
        for j in range(len(s)):
            curr = s[j]
            
            # include current char
            if T[ord(curr)] > 0:
                required -= 1
            T[ord(curr)] -= 1
            
            # 🔥 when valid window
            while required == 0:
                
                # update answer
                curr_len = j - i + 1
                if ans == "" or curr_len < len(ans):
                    ans = s[i:j+1]
                
                # try shrinking
                left = s[i]
                T[ord(left)] += 1
                if T[ord(left)] > 0:
                    required += 1
                
                i += 1
        
        return ans