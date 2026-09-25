class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        answer = 0


        for i in range(len(s)):
            while s[i] in window:
                window.pop(0)
            if s[i] not in window:
                window.append(s[i])
            
            answer = max(answer, len(window))
        
        return answer
            

            
