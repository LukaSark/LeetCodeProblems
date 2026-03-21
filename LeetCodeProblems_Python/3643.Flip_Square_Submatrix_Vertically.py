class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for offset in range(k // 2):
            top = x + offset
            bot = x + k - 1 - offset
            for j in range(y, y + k):
                grid[top][j], grid[bot][j] = grid[bot][j], grid[top][j]
        return grid