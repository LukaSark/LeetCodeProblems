class Solution:
    def binaryGap(self, n: int) -> int:
        binary = str(bin(n))[2:]

        distance = 0

        for i in range(len(binary)):
            if binary[i] == '1':
                for j in range(i+1, len(binary)):
                    if binary[j] == '1':
                        distance = max(distance, j-i)
                        break

        return distance