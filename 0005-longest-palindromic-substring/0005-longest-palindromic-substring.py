class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestLeft = 0
        longestRight = 0

        def expand(l, r):
            nonlocal longestLeft
            nonlocal longestRight

            while l >= 0 and r < len(s) and s[l] == s[r]:
                currentLength = r - l + 1
                longestLength = longestRight - longestLeft + 1

                if currentLength > longestLength:
                    longestLeft = l
                    longestRight = r
                
                l -= 1
                r += 1
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return s[longestLeft: longestRight + 1]


                    

            