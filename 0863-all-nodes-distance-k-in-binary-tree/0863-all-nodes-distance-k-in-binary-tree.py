class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        def dfs(node, par):
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        temp = deque([(target, 0)])
        vis = set([target])
        ans = []
        while temp:
            curr, lvl = temp.popleft()
            if lvl == k:
                ans.append(curr.val)
            for nxt in [curr.left, curr.right, parent[curr]]:
                if nxt and nxt not in vis:
                    vis.add(nxt)
                    temp.append((nxt, lvl + 1))
        return ans