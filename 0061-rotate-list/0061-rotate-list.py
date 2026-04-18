# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head  
        l = 0
        temp = head
        while temp:
            l += 1
            temp = temp.next
        k = k % l
        if k == 0:
            return head
        t = l - k
        traverse = head
        for x in range(t - 1):
            traverse = traverse.next
        ans = traverse.next
        traverse.next = None   
        dummy = ans
        while dummy.next:
            dummy = dummy.next 
        dummy.next = head
        return ans
         

