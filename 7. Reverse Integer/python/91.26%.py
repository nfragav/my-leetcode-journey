class Solution(object):
    def reverse(self, x):
        lowerBound = -2**31
        upperBound = 2**31  

        negative = False
        string = str(x)
        if x < 0:
            negative = True
            string = str(x)[1:]

        string = string[::-1]
        out = int(string)
        if negative:
            out = -out

        if out < lowerBound or out > upperBound:
            return 0

        return out
