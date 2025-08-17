class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        num = 0
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        while i < n and s[i].isdigit():
            num = num * 10 + (ord(s[i]) - ord('0'))

            if sign * num <= INT_MIN:
                return INT_MIN
            if sign * num >= INT_MAX:
                return INT_MAX

            i += 1

        return sign * num
