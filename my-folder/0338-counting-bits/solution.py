class Solution:
    def countBits(self, n: int) -> List[int]:
        bit = []
        for i in range(n+1):
            print(bin(i))
            bit.append(len(bin(i).replace('0b','').replace('0','')))
        return bit
