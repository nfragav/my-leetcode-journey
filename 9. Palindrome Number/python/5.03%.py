class Solution(object):
    def isPalindrome(self, x):
        intToString = str(x)
        total = len(intToString)
        i = 0
        j = total - 1

        while i <= total // 2 and j >= total // 2:
            if intToString[i] == intToString[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

        