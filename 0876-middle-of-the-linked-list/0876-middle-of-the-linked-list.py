# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0 
        d1 = head 
        while d1 :
            l += 1
            d1 = d1.next 
        mid = l // 2
        idx = 0 
        while idx < mid :
            head = head.next 
            idx += 1
        return head  