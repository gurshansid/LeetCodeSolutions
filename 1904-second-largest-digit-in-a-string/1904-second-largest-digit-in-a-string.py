class Solution(object):
    def secondHighest(self, s):
        nums = set()

        for i in range(len(s)):
            if (s[i].isdigit()):
                nums.add(int(s[i]))
        sorted_nums = sorted(nums)

        if (len(sorted_nums) == 1 or len(sorted_nums) == 0):
            return -1
        return sorted_nums[len(sorted_nums) - 2]

        