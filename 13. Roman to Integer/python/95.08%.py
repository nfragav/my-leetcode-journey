class Solution(object):
    def romanToInt(self, s):
        output = 0
        total = len(s)
        i = 0

        while i < total:
            two_step = False

            if s[i] == 'M':
                output += 1000
            if s[i] == 'D':
                output += 500
            if s[i] == 'C':
                if i + 1 < total:
                    if s[i + 1] == 'D':
                        output += 400
                        two_step = True
                    elif s[i + 1] == 'M':
                        output += 900
                        two_step = True
                if not two_step:
                    output += 100
                    
            if s[i] == 'L':
                output += 50

            if s[i] == 'X':
                if i + 1 < total:
                    if s[i + 1] == 'L':
                        output += 40
                        two_step = True
                    elif s[i + 1] == 'C':
                        output += 90
                        two_step = True
                if not two_step:
                    output += 10

            if s[i] == 'V':
                output += 5
            if s[i] == 'I':
                if i + 1 < total:
                    if s[i + 1] == 'V':
                        output += 4
                        two_step = True
                    elif s[i + 1] == 'X':
                        output += 9
                        two_step = True
                if not two_step:
                    output += 1
            
            if not two_step:
                i += 1
            else:
                i += 2
        
        return output
