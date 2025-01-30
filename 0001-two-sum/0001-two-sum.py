class Solution(object):
    def twoSum(self, nums, target):
        s = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in s:
                return [s[difference], i] 
            else:
                s[nums[i]] = i