class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for x in s :
            if not st or x != '*':
                st.append(x)
            else:
                st.pop()
        return "".join(st)
