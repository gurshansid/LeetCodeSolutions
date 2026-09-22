class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1 = [0] * (len(nums) + 1)
        houses1 = nums[:-1]

        for i in range(len(houses1) - 1, -1, -1):
            dp1[i] = max(houses1[i] + dp1[i + 2], dp1[i + 1])
        
        dp2 = [0] * (len(nums) + 1)
        houses2 = nums[1:]

        for i in range(len(houses2) - 1, -1, -1):
            dp2[i] = max(houses2[i] + dp2[i + 2], dp2[i + 1])
        
        return max(dp1[0], dp2[0])
        
