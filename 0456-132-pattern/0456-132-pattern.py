class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        st = []
        var = float(-inf)

        for x in range(len(nums)-1,-1,-1) :
            if nums[x] < var :
                return True 
            while st and nums[x] > st[-1] :
                var = st[-1]
                st.pop()
            st.append(nums[x])
            print(var)
        
        return False

        