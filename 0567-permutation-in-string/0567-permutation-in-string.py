class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1arr = [0] * 26
        s2arr = [0] * 26
        for x in s1 :
            s1arr[ord(x) - 97] += 1
        for x in range(len(s2)):
            s2arr[ord(s2[x]) - 97] += 1
            if x >= len(s1) :
                s2arr[ord(s2[x - len(s1)]) - 97] -= 1
            if s1arr == s2arr :
                return True 
        return False