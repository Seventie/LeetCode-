# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        dummy = ans 
        carry = 0
        while l1 or l2 or carry :
            _sum = carry 
            if l1 :
                _sum = _sum + l1.val
                l1 = l1.next 
            if l2 :
                _sum = _sum + l2.val 
                l2 = l2.next 
            if _sum > 9 :
                carry = 1 
                _sum = _sum % 10
            else :
                carry = 0 
            dummy.next = ListNode(_sum)
            dummy = dummy.next 
        return ans.next