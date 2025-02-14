class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = []

        for i in range(len(matrix)):
            rows.append([matrix[i][0], matrix[i][len(matrix[i]) - 1]])
        
        left = 0
        right = len(rows) - 1
        rowFound = -1

        while (left <=right):
            middle = (left + right) // 2

            if rows[middle][0] <= target <= rows[middle][1]:
                rowFound = middle
                break
            elif target < rows[middle][0]:
                right = middle - 1
            else:
                left = middle + 1
        
        l = 0
        r = len(matrix[rowFound]) - 1

        while l <= r:
            middle = (l + r) // 2

            if matrix[rowFound][middle] == target:
                return True
    
            elif target < matrix[rowFound][middle]:
                r = middle - 1
        
            else:
                l = middle + 1
        
        return False
        