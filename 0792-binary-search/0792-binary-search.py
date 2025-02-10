class Solution(object):
    def search(self, nums, target):
        high = len(nums) - 1
        low = 0

        while low <= high:
            mid = high + low // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                low = mid + 1

            else: 
                high = mid - 1
        
        return -1
        