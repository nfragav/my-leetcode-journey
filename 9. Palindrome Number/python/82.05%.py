class Solution(object):
    def isPalindrome(self, x):
        intToString = str(x)

        if intToString[::-1] == intToString:
            return True

        return False

        