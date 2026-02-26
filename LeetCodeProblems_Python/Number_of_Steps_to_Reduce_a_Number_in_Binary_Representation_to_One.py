class Solution:
    def numSteps(self, s: str) -> int:
        decimal = int(s, 2)
        steps = 0

        while decimal > 1:
            if decimal % 2 == 0:
                decimal //= 2
                steps += 1
            else:
                decimal += 1
                steps += 1
        
        return steps
        