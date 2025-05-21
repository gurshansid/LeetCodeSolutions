class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        answer = []
        l = 0

        while l < len(s):
            for i in range(l, len(s)):
                substring = s[l:i + 1]
                if (substring.count("0") <= k or substring.count("1") <= k):
                    answer.append(substring)
            l += 1
        return len(answer)