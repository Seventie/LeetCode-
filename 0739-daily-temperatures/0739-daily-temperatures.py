class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]* len(temperatures)   
        st = []
        for x in range(len(temperatures))  :
            while st and temperatures[st[-1]] < temperatures[x] :
                ans[st[-1]] = x - st[-1]
                st.pop()
            st.append(x)
        return ans 