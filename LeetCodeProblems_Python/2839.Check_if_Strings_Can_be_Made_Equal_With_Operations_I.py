class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        s1 = list(s1)

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if i + 2 < len(s1) and s1[i + 2] == s2[i]:
                    # swap i and i+2 in s1
                    s1[i], s1[i + 2] = s1[i + 2], s1[i]
                elif i - 2 >= 0 and s1[i - 2] == s2[i]:
                    # swap i and i-2 in s1
                    s1[i], s1[i - 2] = s1[i - 2], s1[i]
                else:
                    return False

        return s1 == list(s2)