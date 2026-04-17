# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return head 
        ans = ListNode(0)
        res = ans 
        while head :
            curr = head.val 
            if head.next :
                if head.next.val == curr :
                    while head.next and head.next.val == curr :
                        head = head.next 
                else :
                    ans.next = ListNode(curr)
                    ans = ans.next 
            else :
                ans.next = ListNode(curr)
                ans = ans.next 
            head = head.next 
        return res.next 