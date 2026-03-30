class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False


        evens1 = []
        evens2 = []
        odds1 = []
        odds2 = []

        for i in range(len(s1)):
            if i % 2 == 0:
                evens1.append(s1[i])
                evens2.append(s2[i])
            else:
                odds1.append(s1[i])
                odds2.append(s2[i])
        evens1.sort()
        evens2.sort()
        odds1.sort()
        odds2.sort()

        return evens1 == evens2 and odds1 == odds2
        
# Time limit exceeds
        # s1 = list(s1)

        # for i in range(len(s1)):
        #     if s1[i] != s2[i]:
        #         print(s1[i], s2[i])
        #         for j in range(i+1, len(s1)):
        #             if s2[i] == s1[j] and (j-i) % 2 == 0:
        #                 tmp = s1[i]
        #                 s1[i] = s1[j]
        #                 s1[j] = tmp
        #                 break
        
        # return s1 == list(s2)