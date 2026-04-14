class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a = 0 
        b = 0 
        l = 0 
        o = 0
        n = 0
        for x in text :
            if x == 'a':
                a += 1
            elif x == 'b' :
                b += 1
            elif x == 'l':
                l += 1
            elif x == 'o':
                o += 1
            elif x == 'n':
                n += 1
            else:
                pass
        l = l//2 
        o = o//2
        return min(b,a,l,o,n)