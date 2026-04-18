# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        right = ListNode(0)
        left = ListNode(0)
        
        l = left 
        r = right 

        while head :
            if head.val < x :
                l.next = ListNode(head.val)
                l = l.next 
            else :
                r.next = ListNode(head.val)
                r = r.next 
            head = head.next 
        
        if right.next :
            l.next = right.next 
        
        return left.next 
