class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []
        a = len(s)
        b = len(words[0])
        corpus = Counter(words)
        ans = []
        total_words = len(words)
        for x in range(b):
            left = x
            count = 0
            seen = Counter()
            for i in range(x, a, b):   
                word = s[i:i+b]
                if word not in corpus:
                    seen.clear()
                    count = 0
                    left = i + b       
                    continue
                seen[word] += 1        
                count += 1
                while seen[word] > corpus[word]:
                    left_word = s[left:left+b]
                    seen[left_word] -= 1
                    left += b
                    count -= 1
                if count == total_words:
                    ans.append(left)

        return ans
                
