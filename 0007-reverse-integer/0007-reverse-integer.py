class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        new_num = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            if new_num > (2**31 - 1) // 10 or (new_num == (2**31 - 1) // 10 and digit > 7):
                return 0
            if new_num < (-2**31) // 10 or (new_num == (-2**31) // 10 and digit < -8):
                return 0

            new_num = new_num * 10 + digit

        return sign * new_num
