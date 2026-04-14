class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for x in strs :
            y = "".join(sorted(x))
            maps[y].append(x)
        ans = []
        for x,y in maps.items():
            ans.append(y)
        return ans 

