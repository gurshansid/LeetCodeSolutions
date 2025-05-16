class Solution(object):
    def singleNumber(self, nums):
        nums.sort()

        for i in range(len(nums)):
            if len(nums) == 1:
                return nums[i]
            if (i == 0 and nums[i] != nums[i+1]):
                return nums[i]
            elif (i == len(nums) - 1 and nums[i] != nums[i-1]):
                return nums[i]
            elif (nums[i] != nums[i+1] and nums[i] != nums[i-1]):
                return nums[i]