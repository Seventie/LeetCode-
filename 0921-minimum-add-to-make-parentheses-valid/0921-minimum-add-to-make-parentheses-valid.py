class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        _open = 0 
        _close = 0 
        ans = 0 

        for x in s :
            if x == '(' :
                _open += 1
            else :
                if _open > 0 :
                    _open -= 1
                else :
                    _close += 1
        
        return _open + _close 