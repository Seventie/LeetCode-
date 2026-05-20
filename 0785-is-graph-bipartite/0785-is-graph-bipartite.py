class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        _seen = {}

        def dfs(idx, color):
            _seen[idx] = color
            for x in graph[idx]:
                if x in _seen:
                    if _seen[x] == color:
                        return False
                else:
                    if not dfs(x, not color):
                        return False
            return True
        for x in range(len(graph)):
            if x not in _seen:
                if not dfs(x, 0):
                    return False
        return True