class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        answer = 0
        left = 0

        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1

            while ((i - left + 1) - max(freq.values()) > k):
                freq[s[left]] = freq[s[left]] - 1
                left += 1
            
            answer = max(answer, i - left + 1)
        
        return answer
