class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def search(index, arr, _sum):
            if _sum == target:
                ans.append(arr[:])
                return

            for i in range(index, len(candidates)):
                x = candidates[i]

                if _sum + x > target:
                    return

                arr.append(x)
                search(i, arr, _sum + x)  
                arr.pop()

        search(0, [], 0)
        return ans