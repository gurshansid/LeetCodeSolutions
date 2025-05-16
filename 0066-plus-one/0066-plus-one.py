class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No carry, done
            digits[i] = 0  # Set to 0 and carry over

        # If all digits were 9 (e.g., [9,9,9]), add 1 at the start
        return [1] + digits