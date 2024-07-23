class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ''
        i = 0
        while i < len(strs[0]):
            common = True
            current_char = strs[0][i]
            for string in strs:
                if len(string) > i:
                    if string[i] != current_char:
                        common = False
                        break
                else:
                    common = False
                    break

            if common:
                prefix += current_char
            else:
                break
            i += 1
        
        return prefix

