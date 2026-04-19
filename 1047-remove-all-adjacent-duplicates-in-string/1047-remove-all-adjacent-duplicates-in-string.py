class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for x in range(len(s)):
            if not st:
                st.append(s[x])
            elif st[-1] == s[x]:
                st.pop()
            else:
                st.append(s[x])
        return ''.join(st)