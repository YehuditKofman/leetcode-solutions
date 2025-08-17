class Solution(object):
    def xorGame(self, nums):
        all_xor = 0
        n = len(nums)
        for num in nums:
            all_xor ^= num
        if all_xor == 0:
            return True
        if n % 2 == 0:
            return True
        return False