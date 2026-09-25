class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        numbers = sorted(nums)
        answer = set()

        for i in range(len(numbers)):
            left = i + 1
            right = len(numbers) - 1

            while left < right:

                if numbers[i] + numbers[left] + numbers[right] > 0:
                    right -=1
                    continue
                
                if numbers[i] + numbers[left] + numbers[right] < 0:
                    left +=1
                    continue
                
                if numbers[i] + numbers[left] + numbers[right] == 0:
                    answer.add((numbers[i], numbers[left], numbers[right]))
                    left += 1
                    right -= 1
                    continue
        return list(answer)