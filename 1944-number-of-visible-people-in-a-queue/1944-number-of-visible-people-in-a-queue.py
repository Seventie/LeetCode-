class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        st = []

        for i in range(n - 1, -1, -1):
            while st and heights[st[-1]] < heights[i]:
                st.pop()
                ans[i] += 1

            if st:
                ans[i] += 1
            
            st.append(i)
        
        return ans