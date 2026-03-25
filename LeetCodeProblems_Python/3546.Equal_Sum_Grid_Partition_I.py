class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        total = 0

        for row in grid:
            for val in row:
                total += val
        
        rowCutTotal = 0
        # checks row cuts
        for i in range(m):
            rowCutTotal += sum(grid[i])
            if rowCutTotal * 2 == total:
                return True
        
        colCutTotal = 0

        # checks col cuts
        for i in range(n-1):
            colCutTotal += sum(grid[r][i] for r in range(m))
            if colCutTotal * 2 == total:
                return True
            
        return False