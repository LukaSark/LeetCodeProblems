class Solution:
    def minPartitions(self, n: str) -> int:
        partitions = 0
        for i in range(len(n)):
            partitions = max(partitions, int(n[i]))
        
        return partitions