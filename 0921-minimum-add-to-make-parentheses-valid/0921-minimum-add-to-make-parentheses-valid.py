class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        _open = 0 
        _close = 0 
        for x in s :
            if x == '(' :
                _open += 1 
            else :
                if _open <= 0 :
                    _close += 1 
                else :
                    _open -= 1
        return _close + _open 