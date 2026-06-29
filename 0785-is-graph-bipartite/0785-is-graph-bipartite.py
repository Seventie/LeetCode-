class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        vis = {}
        n = len(graph)

        def helper(i, col):
            vis[i] = col
            new_col = not col

            for x in graph[i]:
                if x in vis:
                    if vis[x] != new_col:
                        return False
                else:
                    if not helper(x, new_col):
                        return False
            return True

        for x in range(n):
            if x not in vis:
                if not helper(x, True):
                    return False

        return True