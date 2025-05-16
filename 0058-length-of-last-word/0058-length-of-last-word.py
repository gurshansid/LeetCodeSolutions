class Solution(object):
    def lengthOfLastWord(self, s):
        counter = 0
        for i in range(len(s) - 1, -1, -1):
            if (s[i] != " "):
                counter += 1
                if (s[i - 1] == " "):
                    break
        return counter
        