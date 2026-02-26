class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        for i in range(0, len(str(x))):
            if str(x)[i] != str(x)[-i - 1]:
                return False
        return True