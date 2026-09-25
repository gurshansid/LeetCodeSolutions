class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        answer = 0

        while left < right:
            smaller = min(height[left], height[right])
            total = smaller * (right - left)
            answer = max(answer, total)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return answer


