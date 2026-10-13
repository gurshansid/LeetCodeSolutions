class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_dp = [0] * len(nums) 
        min_dp = [0] * len(nums)

        res = nums[0]
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]


        for i in range(1, len(nums)):
            min_dp[i] = min(nums[i], nums[i] * min_dp[i - 1], nums[i] * max_dp[i - 1])
            max_dp[i] = max(nums[i], nums[i] * min_dp[i - 1], nums[i] * max_dp[i - 1])

            res = max(res, max_dp[i])
        return res