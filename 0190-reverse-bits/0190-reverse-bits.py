class Solution:
    def reverseBits(self, n: int) -> int:
        bit = ""
        while n :
            bit += str(n%2)
            n = n//2
        bits_to_add = 32 - len(bit)
        for x in range(bits_to_add):
            bit+= "0"
        return int(bit,2)