class Solution(object):
    def productExceptSelf(self, nums):
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        result = [1] * len(nums)

        for i in range(len(nums)):
            if (i == 0):
                prefix[i] = 1
            else:
                prefix[i] = nums[i - 1] * prefix[i - 1]
        
        for j in range(len(nums) - 1, -1, -1):
            if (j == len(nums) - 1):
                suffix[j] = 1
            else:
                suffix[j] = nums[j + 1] * suffix[j + 1]       

        for z in range(len(nums)):  
            result[z] = prefix[z] * suffix[z] 

        return result 

        