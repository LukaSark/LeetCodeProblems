class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(string):
            inverted = []
            for i in range(len(string)):
                if string[i] == '0':
                    inverted.append('1')
                else:
                    inverted.append('0')
            return "".join(inverted)

        def reverse(string):
            reversedStr = ""
            for i in range(len(string)):
                reversedStr += string[-i-1]
            return reversedStr
        
        BinaryStr = ""
        for i in range(0, n):
            if i == 0:
                BinaryStr += '0'
            BinaryStr = BinaryStr + "1" + reverse(invert(BinaryStr))

        return str(BinaryStr[k-1])