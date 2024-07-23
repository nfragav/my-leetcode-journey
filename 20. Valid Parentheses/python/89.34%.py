class Solution(object):
    def isValid(self, s):
        opening = ['(', '[', '{']
        closing = [')', ']', '}']

        left = []
        right = []
        valid = True
        for char in s:
            if char in opening:
                left.append(char)
            else:
                if left:
                    if opening.index(left[-1]) == closing.index(char):
                        left.pop()
                    else:
                        right.append(char)
                        valid = False
                else:
                    right.append(char)
                    valid = False
        
        if left or right:
            valid = False
        
        return valid
