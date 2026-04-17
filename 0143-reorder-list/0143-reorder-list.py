class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        temp = head
        while temp:
            nodes.append(temp.val)
            temp = temp.next 
        i = 0 
        j = len(nodes) - 1  
        temp = head
        while temp:
            if i <= j:
                temp.val = nodes[i]
                i += 1
                temp = temp.next
            
            if temp and i <= j:
                temp.val = nodes[j]
                j -= 1
                temp = temp.next