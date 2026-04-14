import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        mp = defaultdict(int)
        for x in s :
            mp[x] += 1
        maxheap = []
        for x ,y in mp.items():
            heapq.heappush(maxheap,(-y,x))
        print(maxheap)
        prev = [-len(s)+1,'#'] 
        ans = ""
        while heap :
            
