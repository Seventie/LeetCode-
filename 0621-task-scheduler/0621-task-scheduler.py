class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        _alpha = [0] * 26 
        for x in tasks :
            _alpha[ord(x)-ord("A")] += 1 
        _alpha.sort()
        c = _alpha[-1] -1 
        idle = c * n 

        for i in range(24,-1,-1) :
            idle -= min(c ,_alpha[i])

        return len(tasks) + idle if idle > 0 else len(tasks)

