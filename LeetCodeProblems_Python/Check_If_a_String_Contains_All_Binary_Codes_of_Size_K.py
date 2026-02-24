# class Solution:
#     def hasAllCodes(self, s: str, k: int) -> bool:
        
#         subStrings = []

#         def dfs(cnt, substring):
#             if cnt == k:
#                 subStrings.append(substring)
#                 return 
#             dfs(cnt + 1, substring + "0")
#             dfs(cnt + 1, substring + "1")

#         dfs(0, "")


#         for code in subStrings:
#             if code not in s:
#                 return False
        
#         return True

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()

        for i in range(len(s) - k+1):
            seen.add(s[i: k+i])
        
        return len(seen) == 2**k