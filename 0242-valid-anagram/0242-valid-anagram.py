class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        firstString = {}
        secondString = {}

        for char in s:
            firstString[char] = firstString.get(char, 0) + 1

        for char in t:
            secondString[char] = secondString.get(char, 0) + 1
        
        return firstString == secondString

        