"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        dummy = head
        while dummy:
            if dummy.child:
                a = dummy.next
                child = self.flatten(dummy.child)
                dummy.next = child
                child.prev = dummy
                dummy.child = None
                temp = dummy.next
                while temp.next:
                    temp = temp.next
                if a:
                    temp.next = a
                    a.prev = temp
                
                dummy = a
            else:
                dummy = dummy.next
        
        return head