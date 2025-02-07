class Solution(object):
    def maxArea(self, height):
        result = 0
        left = 0
        right = len(height) - 1

        while (left < right):
            waterUsed = (right - left) * min(height[left], height[right])
            
            if (result < waterUsed):
                result = waterUsed
            
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        
        return result
        