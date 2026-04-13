class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 :
            return s
        numRows = min(numRows,len(s))
        storage = [""] * numRows
        flag = 1 
        i = 0 
        for x in s :
            storage[i] = storage[i] + x
            if i == 0:
                flag = 1 
            if i == numRows- 1 :
                flag = -1  
            i+=flag 
        return "".join(storage)
            

