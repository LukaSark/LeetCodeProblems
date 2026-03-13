class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        
        def can_finish(time):
            total = 0

            for w in workerTimes:
                x = int((math.sqrt(1+8 * time / w) - 1) // 2)
                total += x

                if total >= mountainHeight:
                    return True
            return False
        
        left, right = 0, 10**18
        while left < right:
            mid = (left+right) // 2

            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left