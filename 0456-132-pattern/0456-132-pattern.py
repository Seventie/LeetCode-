class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st = []
        mid = float('-inf')   # this is the "2" in 132

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < mid:
                return True

            while st and nums[i] > st[-1]:
                mid = st[-1]
                st.pop() 
            st.append(nums[i])     
        return False