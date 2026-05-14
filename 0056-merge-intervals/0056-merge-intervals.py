class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x : x[0])
        ans = []
        _before = intervals[0][0]
        _after  = intervals[0][1]
        ans.append([_before,_after])
        for x in range(1,len(intervals)) :
            curr = intervals[x]
            if  curr[0] <= _after :
                if curr[1] > _after :
                    _after = curr[1]  
                    ans.pop()
                    ans.append([_before,_after])
                    
            else :
                _before = curr[0]
                _after = curr[1]
                ans.append([_before,_after]) 
            
        
        return ans 