class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        sum = 0
        maxSum = 0
        window = set()


        '''
        [4,2,4,5,6]
         l
        '''

        for i in range(len(nums)):
            while nums[i] in window:
                window.remove(nums[l])
                sum -= nums[l]
                l += 1
            window.add(nums[i])
            sum += nums[i]
            maxSum = max(sum, maxSum)
        return maxSum