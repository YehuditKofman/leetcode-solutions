class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[correct_index], nums[i] = nums[i], nums[correct_index]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
