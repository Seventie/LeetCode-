# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = ListNode(0)
        prev.next = head   
        new_head = head.next   
        fake = head
        while fake and fake.next:
            a = fake
            b = fake.next
            
            prev.next = b
            
            temp = b.next
            b.next = a
            a.next = temp
            
            prev = a
            fake = a.next
        
        return new_head






