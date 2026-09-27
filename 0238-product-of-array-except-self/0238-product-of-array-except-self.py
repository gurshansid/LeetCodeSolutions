class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        leftProducts = [nums[0]] * len(nums)
        rightProducts = [nums[len(nums) - 1]] * len(nums)
        answer = [0] * len(nums)

        for i in range(1, len(nums)):
            leftProducts[i] = nums[i] * leftProducts[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            rightProducts[i] = nums[i] * rightProducts[i + 1]
        
        for i in range(len(nums)):
            if i == 0:
                answer[i] = rightProducts[i + 1]
            elif i == len(nums) - 1:
                answer[i] = leftProducts[i - 1]
            else:
                answer[i] = leftProducts[i - 1] * rightProducts[i + 1]
        return answer


