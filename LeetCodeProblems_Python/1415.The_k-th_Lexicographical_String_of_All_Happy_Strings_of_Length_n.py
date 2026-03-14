class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        happyLetters = ['a', 'b', 'c']
        
        happyList = []

        def dfs(string):

            if len(string) == n:
                happyList.append(string)
                return

            for letter in happyLetters:
                if string and letter == string[-1]:
                    continue
                dfs(string+letter)
            
        dfs("")

        if k > len(happyList):
            return "" 
        
        return happyList[k-1]