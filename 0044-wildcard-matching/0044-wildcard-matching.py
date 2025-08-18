class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0
        match = 0
        strIndex = -1
        length = len(p)

        while i < len(s):
            if j < length and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            elif j < length and p[j] == '*':
                match = i
                strIndex = j
                j += 1
            elif strIndex != -1:
                j = strIndex + 1
                match += 1
                i = match
            else:
                return False

        while j < length and p[j] == '*':
            j += 1

        return j == length
