class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        result = 0
        numString = str(num)
        l = 0

        for i in range(k - 1, len(numString)):
            substring = numString[l:i + 1]
            number = int(substring)
            
            if (number != 0 and num % number == 0):
                result += 1
            l += 1
        
        return result




'''
430043
     r
'''