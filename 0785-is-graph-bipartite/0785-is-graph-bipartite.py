class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        def dfs(node, clr):
            if node in color:
                return color[node] == clr
            color[node] = clr
            for nei in graph[node]:
                if not dfs(nei, not clr):
                    return False
            return True
        for node in range(len(graph)):
            if node not in color:
                if not dfs(node, True):
                    return False
        return True