class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        m, n = len(mat), len(mat[0])
        tmp = [row[:] for row in mat]

        for i in range(m):
            if i % 2 == 1:
                for j in range(k):
                    popped = mat[i].pop(len(mat[i]) - 1)
                    mat[i].insert(0, popped)
            else:
                for j in range(k):
                    popped = mat[i].pop(0)
                    mat[i].append(popped)
        
        return mat == tmp

