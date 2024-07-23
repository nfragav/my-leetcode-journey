class Solution(object):
    def intToRoman(self, num):
        string = str(num)
        length = len(string)
        current = length
        output = ''

        while length - current < length:
            digit = int(string[length - current])

            if current == 4:
                output += digit * 'M'

            elif current == 3:
                if digit == 4:
                    output += 'CD'
                elif digit == 9:
                    output += 'CM'
                elif digit >= 5:
                    output += 'D' + (digit % 5) * 'C'
                else:
                    output += digit * 'C'

            elif current == 2:
                if digit == 4:
                    output += 'XL'
                elif digit == 9:
                    output += 'XC'
                elif digit >= 5:
                    output += 'L' + (digit % 5) * 'X'
                else:
                    output += digit * 'X'

            elif current == 1:
                if digit == 4:
                    output += 'IV'
                elif digit == 9:
                    output += 'IX'
                elif digit >= 5:
                    output += 'V' + (digit % 5) * 'I'
                else:
                    output += digit * 'I'

            current -= 1
        
        return output
