class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        concatBinStr = ""
        for i in range(1, n+1):
            binary = str(bin(i)[2:])
            concatBinStr += binary
        
        
        return int(concatBinStr, 2) % (10**9 + 7)