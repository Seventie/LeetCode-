class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        st = []

        for x in nums2:
            while st and x > st[-1]:
                mp[st[-1]] = x
                st.pop()
            st.append(x)

        ans = []
        for x in nums1:
            ans.append(mp.get(x, -1))

        return ans