class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                if (abs(seen[nums[i]] - i) <= k):
                    return True
            seen[nums[i]] = i
        return False
        