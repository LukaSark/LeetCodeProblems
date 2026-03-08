class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        def dfs(string): 
            if string not in nums:
                return string

            for i in range(len(string)):
                if string[i] == '0':
                    new = string[:i] + '1' + string[i+1:]
                    result = dfs(new)
                    if result:
                        return result

        return dfs('0'*len(nums[0]))
