class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.strip().split()
        vowels = {'a', 'e', 'i', 'o', 'u',
                  'A', 'E', 'I', 'O', 'U'}
        for x in range(len(words)):
            if words[x][0] in vowels:
                words[x] += "ma"
            else:
                words[x] = words[x][1:] + words[x][0] + "ma"

            words[x] += 'a' * (x + 1)

        return ' '.join(words)