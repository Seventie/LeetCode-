class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        final = n- 1
        ans = []
        def helper(a, path):
            if a == final :
                ans.append(path[:])
                return 
            for v in graph[a] :
                path.append(v)
                helper(v, path[:])
                path.pop()
        helper(0,[0])
        return ans 