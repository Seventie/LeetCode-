class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x : x[0])
        ans = []
        n = len(intervals)
        i = 0 
        while i < n :
            curr = intervals[i]
            _max = curr[1]
            while i + 1 < n and intervals[i + 1][0] <= _max :
                _max = max(_max, intervals[i + 1][1])
                i += 1
            ans.append([curr[0],_max])
            i += 1
        return ans 
