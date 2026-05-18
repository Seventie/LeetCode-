class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        target = len(graph) -1
        def dfs(idx, path) :
            if idx == target :
                paths.append(path[:])
            for x in graph[idx] :
                path.append(x) 
                dfs(x,path)
                path.pop()
        dfs(0,[0])
        return paths 