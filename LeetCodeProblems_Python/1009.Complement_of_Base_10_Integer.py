class Solution:
    def bitwiseComplement(self, n: int) -> int:

        binary = str(bin(n))[2:]
        complement = ""
        
        for i in range(len(binary)):
            if binary[i] == '1':
                complement += '0'
            else:
                complement += '1'
        
        return int(complement, 2)
        