class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        doubled = s + s
        ans = n

        diff0 = 0
        diff1 = 0

        for i in range(len(doubled)):
            if int(doubled[i]) != i % 2:
                diff0 += 1
            if int(doubled[i]) != (i + 1) % 2:
                diff1 += 1

            if i >= n:
                left = i - n
                if int(doubled[left]) != left % 2:
                    diff0 -= 1
                if int(doubled[left]) != (left + 1) % 2:
                    diff1 -= 1

            if i >= n - 1:
                ans = min(ans, diff0, diff1)

        return ans

        # answer = len(s) # Worst case

        # for rotate in range(len(s)):
        #     rotated = s[rotate:] + s[:rotate]

        #     flips0 = 0 # check to match 101010
        #     flips1 = 0 # check to match 010101

        #     for i in range(len(s)):
        #         if int(rotated[i]) != i % 2:
        #             flips0 += 1
        #         if int(rotated[i]) != (i+1) % 2:
        #             flips1 += 1
            
        #     answer = min(answer, flips0, flips1)
        
        # return answer