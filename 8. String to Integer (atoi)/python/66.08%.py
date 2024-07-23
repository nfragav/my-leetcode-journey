class Solution(object):
    def myAtoi(self, s):
        if s == '':
            return 0
        lowerBound = -2**31
        upperBound = 2**31 - 1
        numbers = [str(n) for n in range(0,10)]
        output = ''
        started = False
        finished = False
        i = 0
        end = len(s)
        while not finished:
            if not started:
                while s[i] == ' ':
                    if i + 1 < end:
                        i += 1
                    else:
                        finished = True
                        break
                if i < end:
                    if s[i] in numbers or s[i] == '-':
                        output += s[i]
                        i += 1
                        started = True
                    else:
                        return 0
                else:
                    return 0
            
            if not finished and started:
                while s[i] in numbers:
                    output += s[i]
                    if i + 1 < end:
                        i += 1
                    else:
                        finished = True
                        break
                finished = True
                

        output = int(output)
        if output < lowerBound:
            return lowerBound
        if output > upperBound:
            return upperBound
        return output

sol = Solution()
print(sol.myAtoi("1"))