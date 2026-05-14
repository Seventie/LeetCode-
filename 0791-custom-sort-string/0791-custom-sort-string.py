class Solution:
    def customSortString(self, order: str, s: str) -> str:
        t = [0] * 26
        tem = [0] * 26
        for x in order :
            t[ord(x)-ord('a')] = 1 
        ans = []
        for x in s :
            if  t[ord(x)-ord('a')] == 0 :
                ans.append(x)
            else :
                tem[ord(x)-ord('a')] += 1 
        leading = []
        for x in order :
            if tem[ord(x)-ord('a')] > 0 :
                for i in range(tem[ord(x)-ord('a')]) :
                    leading.append(x)
        res = ''.join(leading) + ''.join(ans)
        return res