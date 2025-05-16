class Solution(object):
    def reverseString(self, s):
        right = len(s) - 1
        for i in range(len(s)):
            if (i == right or i == right + 1):
                break
            else:
                leftValue = s[i]
                s[i] = s[right]
                s[right] = leftValue
                right -= 1

        
        