class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = []
        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                vals = sorted(set(grid[r][c] for r in range(i, i + k) for c in range(j, j + k)))
                min_diff = float('inf')
                for t in range(1, len(vals)):
                    d = vals[t] - vals[t - 1]
                    if d < min_diff:
                        min_diff = d
                        if min_diff == 0:
                            break
                row.append(min_diff if min_diff != float('inf') else 0)
            ans.append(row)
        return ans