class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        stack = []
        OpenClosed = {"]":"[", "}":"{", ")":"("}

        for char in s:
            if char in OpenClosed:
                if stack and stack[-1] == OpenClosed[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False
        