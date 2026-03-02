class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        steps = 0

        for i in range(n):
            check = grid[i][i+1:]

            if 1 not in check:
                continue
            
            foundValid = False
            for j in range(i+1, n):
                validate = grid[j][i+1:]
                if validate.count(0) == (n - (i+1)):
                    for k in range(j, i, -1):
                        grid[k], grid[k-1] = grid[k-1], grid[k]
                        steps += 1
                    foundValid = True
                    break
            if not foundValid:
                return -1
        
        return steps
