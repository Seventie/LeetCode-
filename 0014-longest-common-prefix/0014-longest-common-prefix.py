class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]

        for x in range(len(word)) :
            for i in strs[1:] :
                if len(i) <= x or word[x] != i[x] :
                    return word[:x]

        return word 
