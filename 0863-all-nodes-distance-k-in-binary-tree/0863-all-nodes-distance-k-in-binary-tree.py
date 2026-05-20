class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        def search(node):
            if not node:
                return None
            if node.left:
                parent[node.left.val] = node
            if node.right:
                parent[node.right.val] = node
            if node.val == target.val:
                return node
            left = search(node.left)
            if left:
                return left
            return search(node.right)
        ans = []
        visited = set()
        def dfs(node, cnt):
            if not node or node.val in visited:
                return
            visited.add(node.val)
            if cnt == k:
                ans.append(node.val)
                return
            if node.val in parent:
                dfs(parent[node.val], cnt + 1)
            dfs(node.left, cnt + 1)
            dfs(node.right, cnt + 1)
        start = search(root)
        dfs(start, 0)
        return ans