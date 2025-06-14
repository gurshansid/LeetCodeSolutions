class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        for i in range(len(s)):
            if s[i] not in s[i + 1:len(s) + 1] and s[i] not in seen:
                return i
            seen.add(s[i])
        return -1
        