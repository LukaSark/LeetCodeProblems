class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        dp_max = [[0]*n for _ in range(m)]
        dp_min = [[0]*n for _ in range(m)]

        dp_max[0][0] = grid[0][0]
        dp_min[0][0] = grid[0][0]

        # first row
        for i in range(1, n):
            dp_max[0][i] = dp_max[0][i-1] * grid[0][i]
            dp_min[0][i] =dp_min[0][i-1] * grid[0][i]
        
        # first col
        for j in range(1, m):
            dp_max[j][0] = dp_max[j-1][0] * grid[j][0]
            dp_min[j][0] = dp_min[j-1][0] * grid[j][0]

        # Fill the rest
        for i in range(1, m):
            for j in range(1, n):
                value = grid[i][j]
                values = [
                    dp_max[i-1][j] * value,
                    dp_min[i-1][j] * value,
                    dp_max[i][j-1] * value,
                    dp_min[i][j-1] * value
                ]

                dp_max[i][j] = max(values)
                dp_min[i][j] = min(values)
        
        result = dp_max[m-1][n-1]
        if result < 0:
            return -1
        return result % MOD