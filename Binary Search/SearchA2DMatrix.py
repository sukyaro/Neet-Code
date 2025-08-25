
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Boolean flag to indicate whether target is found
        found = False  

        # Binary search over the rows (matrix has 'len(matrix)' rows)
        left, right = 0, len(matrix) - 1
        
        # While there are still rows to check and target not found
        while left <= right and not found:
            # Pick the middle row
            midMatrix = (left + right) // 2  
            
            # Check if target exists in the middle row
            if target in matrix[midMatrix]:
                found = True
                return found  # Return immediately if found
            
            # If target is greater than the last element in this row,
            # it must be in a lower row
            elif matrix[midMatrix][-1] < target:
                left = midMatrix + 1  
            
            # Otherwise, target must be in an upper row
            else:
                right = midMatrix - 1  
                
        # If loop finishes without finding target, return False
        return found

    
# A little test of the program    
solution = Solution()
solution1 = solution.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10) # Expecting True
solution2 = solution.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15) # Expecting False


print(solution1)
print(solution2)