class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_val = float('inf')
        negative_count = 0

        for row in matrix:
            for val in row:
                total += abs(val)
                if val < 0:
                    negative_count += 1
                min_val = min(min_val, abs(val))
        
        if negative_count % 2 != 0:
            total -= 2 * min_val
        
        return total