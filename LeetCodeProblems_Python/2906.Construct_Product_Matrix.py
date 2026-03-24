class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        MOD = 12345
        total = n * m

        flatMatrix = []
        for r in grid:
            for val in r:
                flatMatrix.append(val)
        
        prefix = [1] * total
        for i in range(1, total):
            prefix[i] = prefix[i-1] * flatMatrix[i-1] % MOD
        
        suffix = [1] * total
        for i in range(total-2, -1, -1):
            suffix[i] = suffix[i+1] * flatMatrix[i+1] % MOD
        
        result = [[0] * m for _ in range(n)]

        for i in range(total):
            result[i//m][i%m] = prefix[i] * suffix[i] % MOD
        
        return result