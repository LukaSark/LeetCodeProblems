class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()

        for r in range(m):
            for c in range(n):
                sums.add(grid[r][c])

                for size in range(1, min(m, n)):
                    if r -size < 0 or r+size >= m:
                        break
                    if c - size < 0 or c + size >= n:
                        break
                    
                    total = 0
                    for i in range(size):
                        total += grid[r-size+i][c+i]
                        total += grid[r+i][c + size - i]
                        total += grid[r+size-i][c-i]
                        total += grid[r-i][c-size+i]
                    
                    sums.add(total)
        
        return sorted(sums, reverse=True)[:3]