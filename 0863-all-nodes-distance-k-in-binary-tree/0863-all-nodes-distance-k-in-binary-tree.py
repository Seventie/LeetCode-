# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        storage = {}
        def finder(node, val):
            if not node:
                return None

            if node.val == val:
                return node

            if node.left:
                storage[node.left.val] = node
                left = finder(node.left, val)
                if left:
                    return left

            if node.right:
                storage[node.right.val] = node
                right = finder(node.right, val)
                if right:
                    return right

            return None
        ans = []
        visited = set()

        def bfs(node, cnt):
            if not node or node.val in visited:
                return

            visited.add(node.val)

            if cnt == k:
                ans.append(node.val)
                return

            if node.left:
                bfs(node.left, cnt + 1)

            if node.right:
                bfs(node.right, cnt + 1)

            if node.val in storage:
                bfs(storage[node.val], cnt + 1)

        curr = finder(root, target.val)
        bfs(curr, 0)
        return ans 