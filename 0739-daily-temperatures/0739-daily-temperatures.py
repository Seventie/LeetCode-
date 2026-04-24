class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        ans = [0] * n 
        st = []
        for x in range(n) :
            while st and temperatures[x] > temperatures[st[-1]] :
                ans[st[-1]] = x - st[-1]
                st.pop()
            
            st.append(x)
        return ans 