class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        stack = []
        
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(h, height[stack[-1]]) - height[bottom]
                water += distance * bounded_height
            stack.append(i)
        
        return water
