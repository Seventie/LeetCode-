class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans = 0
        seen = set()

        mp = {}

        for emp in employees:
            mp[emp.id] = emp

        def dfs(_id):
            nonlocal ans

            if _id in seen:
                return
            seen.add(_id)
            ans += mp[_id].importance
            for x in mp[_id].subordinates:
                dfs(x)
        dfs(id)
        return ans