class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
        m , n = len(grid), len(grid[0])

        res = 0
        
        x_col = [0] * n
        y_col = [0] * n

        res = 0
        
        for i in range(m):
            x_row = 0
            y_row = 0
            for j in range(n):
                if grid[i][j] == 'X':
                    x_col[j] += 1
                if grid[i][j] == 'Y':
                    y_col[j] += 1
                x_row += x_col[j]
                y_row += y_col[j]
                if x_row > 0 and x_row == y_row:
                    res += 1
        
        return res