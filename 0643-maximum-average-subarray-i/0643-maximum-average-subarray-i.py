class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = nums[:k]
        windowSum = sum(window)
        maxSum = sum(window)

        for i in range(k, len(nums)):
            windowSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, windowSum)
        return maxSum / k

