class Solution(object):
    def longestConsecutive(self, nums):
        numsSet = set(nums)
        longest = 0

        for n in numsSet:
            if (n - 1) not in numsSet:
                length = 1
                while (n + length) in numsSet:
                    length += 1
                longest = max(length, longest)
        return longest
            