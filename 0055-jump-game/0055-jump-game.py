class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxReach = 0
        for i, num in enumerate(nums):
            if i > maxReach:
                return False
            if i + num > maxReach:
                maxReach = i + num
        return True
