import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        mp = defaultdict(int)
        for x in s :
            mp[x] += 1
        heap = []
        for x ,y in mp.items():
            heapq.heappush(heap,[-y,x])
        print(heap)
        prev = [-len(s)+1,'#'] 
        ans = ""
        while heap :
            if not heap :
                break
            current = heap[0]
            ans += current[1]
            current[0] += 1 
            heapq.heappop(heap)
            if prev[1] != '#' and prev[0] < 0:
                heapq.heappush(heap,prev)
            print(ans)
            prev = current 
        if len(ans) != len(s) :
            return ""
        return ans     

