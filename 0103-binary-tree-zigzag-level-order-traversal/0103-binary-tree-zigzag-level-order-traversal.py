# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        store = deque([root])
        flag = 1
        ans = []
        while store :
            n = len(store)
            temp = deque()
            for x in range(n) :
                curr = store[0]
                store.popleft()
                if curr.left :
                    store.append(curr.left)
                if curr.right :
                    store.append(curr.right)
                if flag == 1 :
                    temp.append(curr.val)
                else :
                    temp.appendleft(curr.val)
            ans.append(list(temp))
            flag ^= 1 
        
        return ans 