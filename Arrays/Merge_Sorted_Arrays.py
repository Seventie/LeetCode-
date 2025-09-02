# Intuition
# My first Intution was to use two pointers to traverse through the array and make it happen rather than two loops

# Approach
# Make the array from the back in reverse order so that u needent worry about the elemnts in ur original nums1 array traverse from n+m-1 add elemnts till u have added all the elements in nums2

# Complexity
# Time complexity:
# Time complexity would be O(n+m-1).

# Space complexity:
# Space Complexity is also O(n+m)


''' Code  '''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n -1 
        i = m-1
        j = n-1
        while j >= 0 :
            if (i>= 0 and nums1[i] >=  nums2[j]):
                nums1[k] = nums1[i]
                k-=1
                i-=1
            else :
                nums1[k] = nums2[j]
                k-=1
                j-=1



                
