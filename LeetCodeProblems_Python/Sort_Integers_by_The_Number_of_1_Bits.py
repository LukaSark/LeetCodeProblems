class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        binInt = {}

        for i in range(len(arr)):
            decimal = arr[i]
            binary = str(bin(decimal))[2:]

            count = binary.count('1')
            binInt.setdefault(count, []).append(decimal)
        
        output = []
        for k, v in sorted(binInt.items(), key=lambda item: item[0]):
            for n in sorted(v):
                output.append(n)
            
        return output