# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = 0 
        dummy = head 
        while dummy :
            dummy = dummy.next 
            l += 1
        parts = l//k 
        tail = ListNode(0)
        n = tail
        d2 = head 
        for x in range(parts):
            temp = d2   #1   
            prev = None 
            for j in range(k):
                t2 = d2.next    # 2   3 
                d2.next = prev # 2->1->None
                prev = d2       #2
                d2 = t2        # 3
            tail.next = prev    #0->2->1->None
            tail = temp         #1 
        while d2 :
            tail.next = d2 
            tail = tail.next 
            d2 = d2.next 
        return n.next
            