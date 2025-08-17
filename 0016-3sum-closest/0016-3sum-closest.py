class Solution:
    def oneNum(self, nums, target, first):
        left = first + 1
        right = len(nums) - 1
        closestSum = nums[first] + nums[left] + nums[right]

        while left < right:
            currentSum = nums[first] + nums[left] + nums[right]

            if currentSum == target:
                return target

            if abs(currentSum - target) < abs(closestSum - target):
                closestSum = currentSum

            if currentSum < target:
                left += 1
            else:
                right -= 1

        return closestSum

    def threeSumClosest(self, nums, target):
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        m = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            temp = self.oneNum(nums, target, i)
            if abs(temp - target) < abs(m - target):
                m = temp

        return m
