class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        mp_l = [0] * n
        mp_r = [0] * n
        seen_l = [0] * 26
        seen_r = [0] * 26

        for x in range(n):
            idx = ord(s[x]) - ord('a')
            if not seen_l[idx]:
                mp_l[x] = (mp_l[x-1] + 1) if x > 0 else 1
                seen_l[idx] = 1
            else:
                mp_l[x] = mp_l[x-1]

        for x in range(n - 1, -1, -1):
            idx = ord(s[x]) - ord('a')
            if not seen_r[idx]:
                mp_r[x] = (mp_r[x+1] + 1) if x < n - 1 else 1
                seen_r[idx] = 1
            else:
                mp_r[x] = mp_r[x+1]

        ans = 0
        for i in range(n - 1):        # split after index i
            if mp_l[i] == mp_r[i+1]:
                ans += 1

        return ans
        