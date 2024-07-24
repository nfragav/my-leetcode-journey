class Solution(object):
    def encode(self, string):
        print(string)
        if string == '':
            return ''
        result = ''
        i = 0
        current_digit = string[0]
        count = 1
        while i < len(string):
            if i < len(string) - 1 and current_digit == string[i + 1]:
                count += 1
            else:
                result += '{0}{1}'.format(count, current_digit)
                if i < len(string) - 1 and current_digit != string[i + 1]:
                    current_digit = string[i + 1]
                count = 1
            i += 1
        return result

    def countAndSay(self, n):
        if n == 1:
            return '1'
        else:
            return self.encode(self.countAndSay(n - 1))
        
