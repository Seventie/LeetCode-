class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        ans = []
        def dfs(node, path):
            if node == target:
                ans.append(path[:])   # store a copy
                return
            for nei in graph[node]:
                path.append(nei)
                dfs(nei, path)
                path.pop()
        dfs(0, [0])
        return ans