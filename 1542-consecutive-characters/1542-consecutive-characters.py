class Solution(object):
    def maxPower(self, s):
        # go through each character in s
        # if s[i - 1] is the same as s[i], add 1 to the counter
        # if not, reset counter to 1
        # at each iteration, add counter to arr[i]

        arr = []
        counter = 1

        for i in range(len(s)):
            if i == 0:
                arr.append(counter)
            elif s[i - 1] == s[i]:
                counter = counter + 1
                arr.append(counter)
            else:
                counter = 1
                arr.append(counter)

        return max(arr)

            
