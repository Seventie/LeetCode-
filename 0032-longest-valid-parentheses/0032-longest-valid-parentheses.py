class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        st = [-1]

        for x in range(len(s)):
            if s[x] == '(' :
                st.append(x)
            else :
                st.pop()
                if not st :
                    st.append(x)
                else :
                    ans = max(ans, x-st[-1])
             
        return ans 