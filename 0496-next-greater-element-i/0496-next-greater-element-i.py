class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        st = []

        for x in range(len(nums2)-1,-1,-1) :
            if not st :
                mp[nums2[x]] = -1 
            else :
                while st and nums2[x] > st[-1] :
                    st.pop()
                if not st :
                    mp[nums2[x]] = -1
                else :
                    mp[nums2[x]] = st[-1]
            st.append(nums2[x])

        ans = []
        for x in nums1 :
            ans.append(mp[x])

        return ans 

