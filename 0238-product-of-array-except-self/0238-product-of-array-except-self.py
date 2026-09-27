class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)

        leftProduct = 1

        for i in range(len(nums)):
            answer[i] = leftProduct
            leftProduct = nums[i] * leftProduct
        
        rightProduct = 1

        for i in range(len(nums) - 1, -1, -1):
            answer[i] = rightProduct * answer[i]
            rightProduct = rightProduct * nums[i]
        
        return answer