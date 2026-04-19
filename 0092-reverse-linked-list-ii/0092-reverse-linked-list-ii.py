# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        idx = 1
        prev = None  
        ans = head 
        
        while idx < left:
            idx += 1
            prev = head 
            head = head.next 
        
        tail = head  
        blue = None 

        while idx <= right:
            idx += 1
            temp = head.next 
            head.next = blue
            blue = head
            head = temp 
        if prev:
            prev.next = blue 
        else:
            ans = blue   
        tail.next = head 

        return ans   
