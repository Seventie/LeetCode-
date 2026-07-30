class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 :
            return s 
        n = min(len(s), numRows)
        store = ["" for x in range(n)] 

        flag = False 
        i = 0
        for x in range(len(s)):
            if i == 0 or i == n- 1 :
                flag ^= True 
            if flag :
                store[i] += s[x]
                i += 1
            else :
                store[i] += s[x]
                i -= 1
        return "".join(store)
