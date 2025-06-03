class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        maxLength = 0
        l = 0

        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[l])
                l += 1
            window.add(s[i])
            maxLength = max(maxLength, i - l + 1)
        return maxLength
