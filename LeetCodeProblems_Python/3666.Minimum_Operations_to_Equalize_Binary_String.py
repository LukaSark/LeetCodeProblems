class Solution:
    def minOperations(self, s: str, k: int) -> int:
        
        n = len(s)
        zeros = s.count('0')
        ones = n - zeros

        if ones == n:
            return 0
        
        for i in range(1, n+1):
            p = i * k
            if (p - zeros) % 2 != 0:
                continue
            else:
                if i % 2 == 0:
                    if p >= zeros and p <= (zeros * (i - 1) + ones * i):
                        return i
                else:
                    if p >= zeros and p  <= (zeros * i + ones * (i - 1)):
                        return i

        return -1